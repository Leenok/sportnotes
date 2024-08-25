$(document).ready(function ($) {
	// document.addEventListener('DOMContentLoaded', function() { month,agendaWeek,agendaDay
	var calendar = $("#calendar").fullCalendar({
		header: {
			left: "",
			center: "prev,next",
			right: "title ",
		},
		events: "/all_events",
		selectable: true,
		selectHelper: true,
		editable: true,
		eventLimit: true,
		select: function (start, end, allDay) {
			var title = prompt("Enter Event Title");
			if (title) {
				var start = $.fullCalendar.formatDate(
					start,
					"Y-MM-DD HH:mm:ss"
				);
				var end = $.fullCalendar.formatDate(end, "Y-MM-DD HH:mm:ss");
				$.ajax({
					type: "GET",
					url: "/add_event",
					data: { title: title, start: start, end: end },
					dataType: "json",
					success: function (data) {
						calendar.fullCalendar("refetchEvents");
						alert("Added Successfully");
					},
					error: function (data) {
						alert("There is a problem!!!");
					},
				});
			}
		},
	});
	//   });

	$(".minus").click(function () {
		$(this).closest(".access-line").find(".d-plus").removeClass("hide");
		$(this).closest(".access-line").find(".minus").addClass("hide");
		$(this).closest(".access-line").find(".add-approachs").addClass("hide");
	});
	$(".d-plus").click(function () {
		$(this).closest(".access-line").find(".minus").removeClass("hide");
		$(this)
			.closest(".access-line")
			.find(".add-approachs")
			.removeClass("hide");
		$(this).addClass("hide");
	});
	// add-training-line
	$(".add-training-line").click(function () {
		$(this)
			.closest(".plan-block")
			.find(".form-add-training-line")
			.removeClass("hide");
		$(this).addClass("hide");
	});
	$(".save-training-line").click(function () {
		$(this)
			.closest(".plan-block")
			.find(".form-add-training-line")
			.addClass("hide");
		$(this)
			.closest(".plan-block")
			.find(".add-training-line")
			.removeClass("hide");
	});
	// add-basic_approach
	$(".add-basic_approach").click(function () {
		$(this)
			.closest(".plan-line")
			.find(".form-add-basic_approach")
			.removeClass("hide");
		$(this).addClass("hide");
	});
	$(".save-basic-approach").click(function () {
		$(this)
			.closest(".plan-line")
			.find(".form-add-basic_approach")
			.addClass("hide");
		$(this)
			.closest(".plan-block")
			.find(".add-basic_approach")
			.removeClass("hide");
	});
	// add-new_plan
	$(".add-new_plan").click(function () {
		$(this)
			.closest(".new_plans")
			.find(".form-add-new_plan")
			.removeClass("hide");
		$(this).addClass("hide");
	});
	$(".save-new_plan").click(function () {
		$(this)
			.closest(".new_plans")
			.find(".form-add-new_plan")
			.addClass("hide");
		$(this).closest(".new_plans").find(".add-new_plan").removeClass("hide");
	});
});

function addExercise() {
	console.log("function add Ex");
}
