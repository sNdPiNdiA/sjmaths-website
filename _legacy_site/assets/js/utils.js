/* =========================================
   SHARED UTILITIES
   ========================================= */

export function showToast(message, type = "info") {
    const toast = document.createElement("div");
    toast.innerHTML = message;
    toast.style.cssText = `
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%);
      background: ${type === "error" ? "#e74c3c" : type === "success" ? "#2ecc71" : "#333"};
      color: white;
      padding: 12px 24px;
      border-radius: 50px;
      z-index: 10000;
      font-family: Poppins, sans-serif;
      font-size: 14px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.2);
      animation: fadeIn 0.3s ease forwards;
    `;
    
    // Add animation keyframes if not present
    if (!document.getElementById('toast-style')) {
        const style = document.createElement('style');
        style.id = 'toast-style';
        style.innerHTML = `@keyframes fadeIn { from { opacity: 0; transform: translate(-50%, 20px); } to { opacity: 1; transform: translate(-50%, 0); } }`;
        document.head.appendChild(style);
    }
  
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
  }