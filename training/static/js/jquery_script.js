$( document ).ready(function($) {
    // document.addEventListener('DOMContentLoaded', function() { month,agendaWeek,agendaDay
        var calendar = $('#calendar').fullCalendar({
            header: {
                left:   '',
                center: 'prev,next',
                right:  'title '
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
        $(this).closest('.access-line').find(".d-plus").removeClass('hide');
        $(this).closest('.access-line').find(".minus").addClass('hide');
        $(this).closest('.access-line').find(".add-approachs").addClass('hide');

    })
    $(".d-plus").click(function(){
        $(this).closest('.access-line').find('.minus').removeClass('hide');
        $(this).closest('.access-line').find('.add-approachs').removeClass('hide');
        $(this).addClass('hide');
    })

});

function addExercise(){
    console.log('function add Ex');
}