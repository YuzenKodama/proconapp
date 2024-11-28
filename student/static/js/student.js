function updateTime() {
    const currentTimeElement = document.getElementById('current-time');
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    currentTimeElement.textContent = `現在の時刻: ${hours}:${minutes}:${seconds}`;
}

// 1秒ごとにupdateTime関数を実行して時刻を更新
setInterval(updateTime, 1000);