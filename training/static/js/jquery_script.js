$( document ).ready(function() {
    console.log( "ready! jquery" );
    // $( ".access-add" ).click(function() {

    //     $curr =  $(".access-add").before();
    //     $(`     
    //         <div class="add-approachs">
    //             <p>Подход</p>
    //             <form method="POST">
    //                 {% csrf_token %}
    //                 <input type="hidden" name='training_id' value="{{item.id}}">
    //                 <input type="hidden" name='programm_id' value="{{i.id}}">
    //                 {{ form.number }}<br> 
    //                 {{ form.quantity }}<br> 
    //                 {{ form.weight }}<br> 
    //                 {{ form.time }}<br> 
    //                 {{ form.time_rest }}<br> 

    //                 <span>{{data.error}}</span>
    //                 <button type="submit">Сохранить</button>
    //             </form>
    //         </div>
    //     `).insertBefore(this);


    // });

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