$( document ).ready(function() {
    // document.addEventListener('DOMContentLoaded', function() {
        var calendar = $('#calendar').fullCalendar({
            header: {
                left: 'month,agendaWeek,agendaDay',
                center: 'title',
                right: 'prev,next today'
            },
            events: '/all_events',
            selectable: true,
            selectHelper: true,
            editable: true,
            eventLimit: true,
            select: function (start, end, allDay) {
                var title = prompt("Enter Event Title");
                if (title) {
                    var start = $.fullCalendar.formatDate(start, "Y-MM-DD HH:mm:ss");
                    var end = $.fullCalendar.formatDate(end, "Y-MM-DD HH:mm:ss");
                    $.ajax({
                        type: "GET",
                        url: '/add_event',
                        data: {'title': title, 'start': start, 'end': end},
                        dataType: "json",
                        success: function (data) {
                            calendar.fullCalendar('refetchEvents');
                            alert("Added Successfully");
                        },
                        error: function (data) {
                            alert('There is a problem!!!');
                        }
                    })
                }
            }
        });
    //   });

    $(".minus").click(function(){
        $(".add-approachs").addClass('hide');
        $(".d-plus").removeClass('hide');
        $(".minus").addClass('hide');
    })
    $(".d-plus").click(function(){
        $(".add-approachs").removeClass('hide');
        $(".minus").removeClass('hide');
        $(".d-plus").addClass('hide');

    })



});

function addExercise(){
    console.log('function add Ex');
}