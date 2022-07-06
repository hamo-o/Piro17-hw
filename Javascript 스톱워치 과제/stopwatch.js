const title = document.querySelector("#title");

const start_btn = document.querySelector("#btn-start");
const stop_btn = document.querySelector("#btn-stop");
const reset_btn = document.querySelector("#btn-reset");

const mytime = document.querySelector("#watch-time");

const record_head = document.querySelector("#record-header");

let header_circle = document.querySelector(".fa-circle");
const trash = document.querySelector(".fa-trash-can");

let check;
let circle;

const record_lists = document.querySelector("#record-times");
const record_list = record_lists.getElementsByTagName("li");

let time = 0;
let startTime = 0;
let endTime = 0;
let timer = 0;
let sec = 0;
let msec = 0;

let select = 0;
let target = 0;

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
  newItem.className = "record-time";
  newItem.innerHTML = `
        <i class="fa-regular fa-circle"></i>
        <span>${sec}:${msec}</span>
        <span></span>
    `;
  record_lists.appendChild(newItem);
}

function selectAll() {
  if (select == 0) {
    check = document.createElement("i");
    check.className = "fa-regular fa-circle-check";
    record_head.replaceChild(check, header_circle);

    let i = 0;
    while (record_list[i]) {
      check = document.createElement("i");
      check.className = `fa-regular fa-circle-check`;
      record_list[i].replaceChild(check, record_list[i].firstElementChild);
      i++;
    }
    select = 1;
    header_check = document.querySelector(".fa-circle-check");
  }
}

function deleteListAll() {
  if (select == 1) {
    while (record_lists.hasChildNodes()) {
      record_lists.removeChild(record_lists.firstChild);
    }

    record_head.replaceChild(header_circle, header_check);

    select = 0;
  } else if (select == 2) {
    record_lists.removeChild(target);
  }
}

start_btn.addEventListener("click", start);
stop_btn.addEventListener("click", stop);
reset_btn.addEventListener("click", reset);

header_circle.addEventListener("click", selectAll);
trash.addEventListener("click", deleteListAll);

record_lists.addEventListener("click", (e) => {
  check = document.createElement("i");
  check.className = `fa-regular fa-circle-check`;
  target = e.target.parentNode;
  target.replaceChild(check, target.firstElementChild);

  select = 2;
});
