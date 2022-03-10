let ammount = 2
let x = 'Free response'
function onconfirm(){
  if (window.confirm('Doest thou wish to logout')){
   window.location.replace("/Logout")

  }
}
function loaderr(a){ 
  console.log(a)
 $.getJSON("getjson3/"+a, function(result){
for (let i = 0; i < result.length; i++) {
   let html = `<div class=" mb-3 mt-3 card entry-card">
  <div class="card-header name ">${result[i][0]}</div>
  <div class="card-body "><small>by</small> ${result[i][1]}</div>
  <button type='button' class='btn btn-outline' onclick = 'window.location.replace(/quihz/+${result[i][2]})'>Take</button>
  </div>`
  $('#listoft').append(html)
  }
})}


function teset(n){
  let p = document.getElementById('ammount_selector_'+n).value
  let one = document.getElementById('mc1_'+n)
  let two = document.getElementById('mc2_'+n)
  let three = document.getElementById('mc3_'+n)
  let four = document.getElementById('mc4_'+n)
  let five = document.getElementById('mc5_'+n)
  let six = document.getElementById('mc6_'+n)
  switch(p){
    case '1':
    one.style.display = 'inline'
    two.style.display= 'none'
    three.style.display= 'none'
    four.style.display= 'none'
    five.style.display= 'none'
    six.style.display= 'none'
    break;
    case '2':
    one.style.display = 'inline'
    two.style.display= 'inline'
    three.style.display= 'none'
    four.style.display= 'none'
    five.style.display= 'none'
    six.style.display= 'none'
    break;
    case '3':
    one.style.display = 'inline'
    two.style.display= 'inline'
    three.style.display= 'inline'
    four.style.display= 'none'
    five.style.display= 'none'
    six.style.display= 'none'
    break;
    case '4':
    one.style.display = 'inline'
    two.style.display= 'inline'
    three.style.display= 'inline'
    four.style.display= 'inline'
    five.style.display= 'none'
    six.style.display= 'none'
    break;
    case '5':
    one.style.display = 'inline'
    two.style.display= 'inline'
    three.style.display= 'inline'
    four.style.display= 'inline'
    five.style.display= 'inline'
    six.style.display= 'none'
    break;
    case '6':
    one.style.display = 'inline'
    two.style.display= 'inline'
    three.style.display= 'inline'
    four.style.display= 'inline'
    five.style.display= 'inline'
    six.style.display= 'inline'
    break;
  }
}
function testing(n){
  let f = 'q-'+n
  let x = document.getElementById(f).value
  let v = document.getElementById('quiz_answer_11_'+n)
  let b = document.getElementById('true_'+n)
  let m = document.getElementById('multiple_'+n)
  switch(x){
    case 'Multiple choice':
    v.style.display = 'inline'
    b.style.display = 'none' 
    m.style.display = 'inline'
    break;
    case 'Free response':
    v.style.display = 'inline'
    b.style.display = 'none'
    m.style.display = 'none'
    break;
    case 'True/False':
    v.style.display = 'none'
    b.style.display = 'inline'
    m.style.display = 'none'
    break;
  }
}

function addd(){
  ammount+=1
  let b = document.getElementById('submit')
  b.remove()
  let html = `<div class="qcard card" id='${ammount}'>
  <div class='card-body cahrd'>
<button class="closeb btn btn-outline" type='button' onclick='$("#${ammount}").remove()\'>x</button> 
<br>
  <label for="quantity">Question worth:</label>
    <br>

  <input type="number" id="quantity_${ammount}" name="quantity_${ammount}" min="1" max="100" step="1" value='10' class ='worth mb-3 mt-3'>
    <label for='quiz_name' class="question form-label" id = 'quiz_question_${ammount}' onchange="testing()"> Question type:
    <select class="form-select mt-3 mb-3" id='q-${ammount}' onchange="testing(${ammount})" name='type_${ammount}'>
    <option>Free response</option>
    <option>Multiple choice</option>
    <option>True/False</option>
    </select>
    <label for='quiz_name' class="question form-label" id = 'quiz_question_${ammount}'> Question:
    <input type='quiz_name' class="question form-control" id ="quiz_question_${ammount}" name="question_name${ammount}" required>  
  <div id = 'answer'>
    <div id= 'fr'>
        <label for='quiz_name' class="question form-label" > Answer:
        <input type='quiz_answer' class="question form-control" id ="quiz_answer_11_${ammount}" name="question_answer_fr_${ammount}">  
  </div>
  <div id= 'multiple_${ammount}' class='multiple'>
      <label for='quiz_name' class="question form-label" id = 'hihi' onchange="teset(${ammount})"> Question amount:
    <select class="form-select mt-3 mb-3" onchange="testing(${ammount})" id='ammount_selector_${ammount}' name='ammount_of_${ammount}'>
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    <option>5</option>
    <option>6</option>
    </select>
    <label for='quiz_name' class="question form-label" id = 'mc1_${ammount}' name='mc1_${ammount}'> #1:
    <input type='quiz_answer' class="question form-control" id ="quiz_answer_111" name='mc1_${ammount}'>  
    <label for='quiz_name' class="mc question form-label" id = 'mc2_${ammount}' > #2:
    <input name='mc2_${ammount}' type='quiz_answer' class="mc question form-control" id ="quiz_answer_111">  
    <label for='quiz_name' class="mc question form-label" id = 'mc3_${ammount}'> #3:
    <input name='mc3_${ammount}' type='quiz_answer' class="mc question form-control" id ="quiz_answer_111">  
    <label for='quiz_name' class="mc question form-label" id = 'mc4_${ammount}'> #4:
    <input name='mc4_${ammount}'type='quiz_answer' class="mc question form-control" id ="quiz_answer_111">  
    <label for='quiz_name' class="mc question form-label" id = 'mc5_${ammount}' #5:>
    <input name='mc5_${ammount}' type='quiz_answer' class="mc question form-control" id ="quiz_answer_111">  
    <label for='quiz_name' class="mc question form-label" id = 'mc6_${ammount}'name='mc6_${ammount}'> #6:
    <input name='mc6_${ammount}' type='quiz_answer' class="mc question form-control" id ="quiz_answer_111" name="quiz answer">  
  </div>
  <div id = 'true_${ammount}' class='true'>
    <div class="form-check" id='1'>
    <input type="radio" class="form-check-input" id="radio1" name="t/f_${ammount}" value="True"  name ='true1' checked>True
    <label class="form-check-label" for="radio1"></label>
    </div>
    <div class="form-check" id='2'>
    <input type="radio" class="form-check-input" id="radio2" name="t/f_${ammount}" value="False">False</input>
    <label class="form-check-label" for="radio2"></label>
    </div>
  </div>
</div>
</div>
<button class="buttn btn-outline" type='button' onclick="addd()">+</button> 
</div>
 <button id='submit' type="submit"class="btn btn-outline-primary btn-block">Submit</button><br>
 `
$('#quiz').append(html)
}