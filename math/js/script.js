let data = [];

document.getElementById("addBtn").addEventListener("click", addNumber);
document.getElementById("clearBtn").addEventListener("click", clearAll);
document.getElementById("calculateBtn").addEventListener("click", calculateStats);

function addNumber() {
  const input = document.getElementById("numberInput");
  const value = Number(input.value);

  if (isNaN(value) || input.value === "") {
    alert("⚠️ Please enter a valid number!");
    return;
  }

  data.push(value);
  input.value = "";
  displayData();
}

function displayData() {
  const list = document.getElementById("dataList");
  list.innerHTML = "";

  data.forEach((num, i) => {
    const item = document.createElement("div");
    item.classList.add("data-item");
    item.textContent = num;
    item.style.animationDelay = `${i * 0.05}s`;
    list.appendChild(item);
  });
}

function clearAll() {
  data = [];
  document.getElementById("dataList").innerHTML = "";
  document.getElementById("results").innerHTML = "";
}

function calculateStats() {
  if (data.length === 0) {
    alert("⚠️ Please enter at least one number!");
    return;
  }

  const mean = data.reduce((a, b) => a + b, 0) / data.length;

  const sorted = [...data].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  const median = sorted.length % 2 !== 0
    ? sorted[mid]
    : (sorted[mid - 1] + sorted[mid]) / 2;

  const freq = {};
  let maxFreq = 0;
  sorted.forEach(num => {
    freq[num] = (freq[num] || 0) + 1;
    maxFreq = Math.max(maxFreq, freq[num]);
  });

  const mode = Object.keys(freq)
    .filter(num => freq[num] === maxFreq && maxFreq > 1)
    .map(Number);
  const modeStr = mode.length ? mode.join(", ") : "No mode";

  const variance = data.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / data.length;
  const stdDev = Math.sqrt(variance);

  const resultBox = document.getElementById("results");
  resultBox.innerHTML = `
    <strong>📈 Results:</strong><br>
    ➤ Mean: <b>${mean.toFixed(3)}</b><br>
    ➤ Median: <b>${median}</b><br>
    ➤ Mode: <b>${modeStr}</b><br>
    ➤ Variance: <b>${variance.toFixed(3)}</b><br>
    ➤ Standard Deviation: <b>${stdDev.toFixed(3)}</b>
  `;
  resultBox.style.animation = "none";
  setTimeout(() => resultBox.style.animation = "fadeUp 0.8s ease forwards", 50);
}
