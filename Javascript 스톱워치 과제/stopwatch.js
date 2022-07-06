const title = document.querySelector("#title");
const start_btn = document.querySelector("#btn-start");
const stop_btn = document.querySelector("#btn-stop");
const reset_btn = document.querySelector("#btn-reset");

const mytime = document.querySelector("#watch-time");

let startTime = 0;

title.addEventListener("click", () => {
  window.location.reload();
});

function start() {
  startTime = Date.now();
  setInterval(go, 1);
}

function go() {
  let time = new Date(Date.now() - startTime);

  let sec = addZero(time.getSeconds());
  let msec = addZero(time.getMilliseconds());

  mytime.innerHTML = `<h1>${sec}:${msec}</h1>`;
}

function stop() {
  mytime.innerHTML = `<h1>${time}</h1>`;
}

function reset() {
  stop();
  mytime.innerHTML = `<h1>00:00</h1>`;
}

function addZero(num) {
  if (num < 10) return "0" + num;
}

start_btn.addEventListener("click", start);
stop_btn.addEventListener("click", stop);
reset_btn.addEventListener("click", reset);
