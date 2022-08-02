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

window.onload = function () {
	var h = document.getElementById("hideBtn");
	var op = document.getElementById("openBtn");
	var ct = document.getElementById("checktext");

	h.onclick = function () {
		ct.style.display = "none";
	};

	op.onclick = function () {
		ct.style.display = "block";
		ct.style.fontSize = "20pt";
	};
};
