function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    const currentTime = `${hours}:${minutes}:${seconds}`;
    
    document.getElementById('clock').innerText = currentTime;
}

function handleButtonClick(status) {
    alert(`${status}で登録されました`);
    // ここにさらに処理を追加できます（例：サーバーへの送信など）
}

// 初回表示
updateClock();
// 1秒ごとに更新
setInterval(updateClock, 1000);