$( document ).ready(function() {
    console.log( "ready! jquery" );
    $( ".access-add" ).click(function() {
        console.log('add access');
        $curr =  $(".access-add").before();
        $(`     
        <div class="access">
            <form action="" class="access-item">
                <label for="">Подход 6</label>
                <input type="number" placeholder="km">
                <input type="number" placeholder="time">
                <input type="button" value="delete" class="access-delete">
            </form>
        </div>
        `).insertBefore(this);


    });

    $( ".exercise-add").click(function() {
        console.log('add exc');
        $(`
        <div class="trainings-main">
            <form action="" class="exercise-line">
                <form ac class="exercise">
                    <select id="exerc" name="exerc" class="">
                        <option value="run">Run</option>
                        <option value="jump">Jump</option>
                        <option value="throw">Throw</option>
                    </select>
                </form>
                <div class="access-line">
                    <div class="access">
                        <form action="" class="access-item">
                            <label for="">Подход 1</label>
                            <input type="number" placeholder="km">
                            <input type="number" placeholder="time">
                            <input type="button" value="delete" class="access-delete">
                        </form>
                    </div>
                </div>
                <div class="access-add">
                    <input type="button" value="+" class="plus">
                </div>
                <div class="exercise-total">
                    <div class="bold">Сумма подходов:</div>
                    <div class="">30 km</div>
                    <div class="">1час 15мин</div>
                </div>
            </form>
        </div>
        `).appendTo(".lines");

    });
    



});

function addExercise(){
    console.log('function add Ex');
}