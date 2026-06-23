function toggleSolution(btn){
  const sol = btn.nextElementSibling;
  if(sol.style.display === "block"){
    sol.style.display = "none";
    btn.textContent = "Show Step-by-Step Solution";
  } else {
    sol.style.display = "block";
    btn.textContent = "Hide Step-by-Step Solution";
  }
}
