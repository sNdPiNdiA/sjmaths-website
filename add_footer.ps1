# Add footer and bottom navigation to exercise files
$basePath = "c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

$footer = @'
<div class="bottom-nav">
  <a href="../index.html" class="nav-btn btn-prev">← Back to Exercises</a>
  <a href="../../" class="nav-btn btn-next">Back to Class 10 →</a>
</div>

<footer class="page-footer">
  <div class="footer-content">
    <a href="/">Home</a>
    <a href="/pages/contact.html">Contact</a>
    <a href="/pages/privacy-policy.html">Privacy</a>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 SJMaths</p>
  </div>
</footer>

<div class="floating-controls">
  <a href="../../" class="back-btn-floating">
    <i class="fas fa-arrow-left"></i> Back to Class 10
  </a>
  <button class="theme-toggle-btn" onclick="toggleTheme()" aria-label="Toggle Dark Mode">
    <i class="fas fa-moon"></i>
  </button>
</div>

<script>
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

function toggleTheme() {
  document.body.classList.toggle('dark-mode');
  const icon = document.querySelector('.theme-toggle-btn i');
  if (document.body.classList.contains('dark-mode')) {
    icon.classList.remove('fa-moon');
    icon.classList.add('fa-sun');
    localStorage.setItem('theme', 'dark');
  } else {
    icon.classList.remove('fa-sun');
    icon.classList.add('fa-moon');
    localStorage.setItem('theme', 'light');
  }
}

// Check saved theme
if (localStorage.getItem('theme') === 'dark') {
  document.body.classList.add('dark-mode');
  document.querySelector('.theme-toggle-btn i').classList.replace('fa-moon', 'fa-sun');
}
</script>
'@

Get-ChildItem -Path $basePath -Filter "exercise-*.html" -Recurse | ForEach-Object {
    $filePath = $_.FullName
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    
    # Check if footer already exists
    if ($content -notmatch '<footer class="page-footer">') {
        # Remove closing body tag and replace with footer + closing tags
        $content = $content -replace '</body>\s*</html>\s*$', ($footer + "`n`n</body>`n</html>")
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Added footer: $($_.Name)"
    } else {
        Write-Host "Skip: $($_.Name) (footer exists)"
    }
}
