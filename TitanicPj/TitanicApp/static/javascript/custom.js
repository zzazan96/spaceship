var swiper = new Swiper(".mySwiper", {
  pagination: {
    el: ".swiper-pagination",
    type: "progressbar",
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

// $("input[name=shop]").click(function () {
//   if (this.id == "openBtn3") {
//     $("#checktext3").show("slow");
//   } else {
//     $("#checktext3").hide("slow");
//   }
// });

$(document).ready(function () {
  $("#hideBtn").click(function () {
    $("#checktext").hide();
  });
  $("#openBtn").click(function () {
    $("#checktext").show();
  });
});

$(document).ready(function () {
  $("#hideBtn2").click(function () {
    $("#checktext2").hide();
  });
  $("#openBtn2").click(function () {
    $("#checktext2").show();
  });
});

$(document).ready(function () {
  $("#hideBtn3").click(function () {
    $("#checktext3").hide();
  });
  $("#openBtn3").click(function () {
    $("#checktext3").show();
  });
});

$(document).ready(function () {
  $("#hideBtn4").click(function () {
    $("#checktext4").hide();
  });
  $("#openBtn4").click(function () {
    $("#checktext4").show();
  });
});

$(document).ready(function () {
  $("#hideBtn5").click(function () {
    $("#checktext5").hide();
  });
  $("#openBtn5").click(function () {
    $("#checktext5").show();
  });
});

// function showdiv1(element) {
//   var h = document.getElementById("hideBtn");
//   var op = document.getElementById("openBtn");
//   var ct = document.getElementById("checktext");

//   h.onclick = function () {
//     ct.style.display = "none";
//   };

//   op.onclick = function () {
//     ct.style.display = "block";
//     ct.style.fontSize = "20pt";
//   };
// }

// function showdiv2(element) {
//   var h2 = document.getElementById("hideBtn2");
//   var op2 = document.getElementById("openBtn2");
//   var ct2 = document.getElementById("checktext2");

//   h2.onclick = function () {
//     ct2.style.display = "none";
//   };

//   op2.onclick = function () {
//     ct2.style.display = "block";
//     ct2.style.fontSize = "20pt";
//   };
// }

// function showdiv3(element) {
//   var h3 = document.getElementById("hideBtn3");
//   var op3 = document.getElementById("openBtn3");
//   var ct3 = document.getElementById("checktext3");

//   h3.onclick = function () {
//     ct3.style.display = "none";
//   };

//   op3.onclick = function () {
//     ct3.style.display = "block";
//     ct3.style.fontSize = "20pt";
//   };
// }

// window.onload = function () {
//   var h4 = document.getElementById("hideBtn4");
//   var op4 = document.getElementById("openBtn4");
//   var ct4 = document.getElementById("checktext4");

//   h4.onclick = function () {
//     ct4.style.display = "none";
//   };

//   op4.onclick = function () {
//     ct4.style.display = "block";
//     ct4.style.fontSize = "20pt";
//   };
// };

// window.onload = function () {
//   var h5 = document.getElementById("hideBtn5");
//   var op5 = document.getElementById("openBtn5");
//   var ct5 = document.getElementById("checktext5");

//   h5.onclick = function () {
//     ct5.style.display = "none";
//   };

//   op5.onclick = function () {
//     ct5.style.display = "block";
//     ct5.style.fontSize = "20pt";
//   };
// };
