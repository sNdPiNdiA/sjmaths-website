import { auth, db } from "./firebase-config.js";
import { doc, getDoc, setDoc } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";

export function initStudyPlanner() {
    const input = document.getElementById('new-goal-input');
    const addBtn = document.getElementById('add-goal-btn');
    const list = document.getElementById('goals-list');
    const progressBar = document.getElementById('planner-progress');
    const progressLabel = document.getElementById('progress-label');
    const progressFraction = document.getElementById('progress-fraction');

    if (!input || !list) return; // Guard clause

    let goals = [];
    let currentUser = null;

    // Save Logic (Cloud + Local Fallback)
    const save = async () => {
        if (currentUser) {
            try {
                await setDoc(doc(db, "users", currentUser.uid), {
                    studyGoals: goals
                }, { merge: true });
            } catch (e) {
                console.error("Error syncing goals:", e);
            }
        } else {
            localStorage.setItem('sjmaths_study_goals', JSON.stringify(goals));
        }
        render();
    };

    const render = () => {
        list.innerHTML = '';
        let completed = 0;

        if (goals.length === 0) {
            list.innerHTML = '<li class="empty-state">No goals set for this week. Add one to get started!</li>';
        }

        goals.forEach((goal, index) => {
            if (goal.done) completed++;
            const li = document.createElement('li');
            li.className = `goal-item ${goal.done ? 'done' : ''}`;
            li.innerHTML = `
                <label class="goal-label">
                    <input type="checkbox" ${goal.done ? 'checked' : ''} data-index="${index}">
                    <span class="custom-checkbox"></span>
                    <span class="goal-text">${goal.text}</span>
                </label>
                <button class="delete-goal" data-index="${index}" title="Delete Goal"><i class="fas fa-trash"></i></button>
            `;
            list.appendChild(li);
        });

        // Update Progress
        const total = goals.length;
        const percent = total === 0 ? 0 : Math.round((completed / total) * 100);
        
        if (progressBar) progressBar.style.width = `${percent}%`;
        if (progressLabel) progressLabel.textContent = `${percent}% Completed`;
        if (progressFraction) progressFraction.textContent = `${completed}/${total}`;
    };

    const addGoal = () => {
        const text = input.value.trim();
        if (!text) return;
        goals.push({ text, done: false, createdAt: Date.now() });
        save();
        input.value = '';
    };

    addBtn.addEventListener('click', addGoal);
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') addGoal();
    });

    list.addEventListener('click', (e) => {
        if (e.target.tagName === 'INPUT') {
            const index = e.target.dataset.index;
            goals[index].done = e.target.checked;
            save();
        } else if (e.target.closest('.delete-goal')) {
            const index = e.target.closest('.delete-goal').dataset.index;
            goals.splice(index, 1);
            save();
        }
    });

    // Initialize with Auth Check
    onAuthStateChanged(auth, async (user) => {
        currentUser = user;
        if (user) {
            // Load from Firestore
            try {
                const docSnap = await getDoc(doc(db, "users", user.uid));
                if (docSnap.exists() && docSnap.data().studyGoals) {
                    goals = docSnap.data().studyGoals;
                } else {
                    // Migrate local goals to cloud if first time
                    const localGoals = JSON.parse(localStorage.getItem('sjmaths_study_goals'));
                    if (localGoals && localGoals.length > 0) {
                        goals = localGoals;
                        save(); // Sync to cloud
                        localStorage.removeItem('sjmaths_study_goals');
                    }
                }
            } catch (e) { console.error("Error loading goals:", e); }
        } else {
            goals = JSON.parse(localStorage.getItem('sjmaths_study_goals')) || [];
        }
        render();
    });
}