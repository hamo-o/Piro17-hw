const title = document.querySelector("#title");

const start_btn = document.querySelector("#btn-start");
const stop_btn = document.querySelector("#btn-stop");
const reset_btn = document.querySelector("#btn-reset");

const mytime = document.querySelector("#watch-time");
const container = document.querySelector("#record-times");

let time = 0;
let startTime = 0;
let endTime = 0;
let timer = 0;
let sec = 0;
let msec = 0;

title.addEventListener("click", () => {
  window.location.reload();
});

function go() {
  time = new Date(Date.now() - startTime);

  sec = addZero(time.getSeconds());
  msec = addZero(parseInt(time.getMilliseconds() / 10));

  mytime.innerHTML = `<h1>${sec}:${msec}</h1>`;
}

function start() {
  if (endTime == 0) {
    startTime = Date.now();
  } else {
    startTime = Date.now() - endTime;
  }
  timer = setInterval(go, 1);
}

function stop() {
  endTime = time;
  clearInterval(timer);
  mytime.innerHTML = `<h1>${sec}:${msec}</h1>`;
  addList();
}

function reset() {
  clearInterval(timer);
  mytime.innerHTML = `<h1>00:00</h1>`;
}

function addZero(num) {
  if (num < 10) {
    return "0" + num;
  } else {
    return num;
  }
}

function addList() {
  const newItem = document.createElement("li");
  newItem.innerHTML = `
  <div class="record-time">
        <i class="fa-regular fa-circle"></i>
        <span>${sec}:${msec}</span>
        <span></span>
      </div>
    `;
  container.appendChild(newItem);
}

start_btn.addEventListener("click", start);
stop_btn.addEventListener("click", stop);
reset_btn.addEventListener("click", reset);
