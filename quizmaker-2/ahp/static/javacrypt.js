var  a = 1
var ttt =''
function render(i,r) {
try{
  switch (i[1]) {
    case 'Multiple choice':
      console.log('multiple choice')
      let y = 7
    console.log(i[2])
    r.push(i[2])
    console.log(i[1])
      $('#quiz').append(`<p class='q frqq f bb${a}'> ${i[0]}</p><div  class='bb${a}' id='bb${a}'></div>`)
      for (let pp = 0; pp < y; pp++) {
          $('#bb'+a).append(`<div class="q cb bb${a}">
    <input type="radio" class="form-check-input mco q bb${a}" id="bb${a}" name="${i[2]}" value="${r[pp]} " >${r[pp]}</input>
    </div>`)
        }
      console.log(a)
       a +=1
      break;
    case 'True/False':
      console.log('true or false')
      $('#quiz').append(`<p class='q frq bb${a}'>${i[0]}</p><div class='q ff bb${a} f'>
    <div class="q tt bb${a}">
    <input type="radio" class="form-check-input q bb${a}" id="radio1"  value="True"  name ='${i[2]}' checked>True
    <label class=" q bb${a} form-check-label" for="radio1"></label>
    </div>
    <div class="q tt form-check bb${a}" id='2'>
    <label class="q bb${a} form-check-label" for="radio2"></label>
    <input type="radio" class="q  t bb${a} form-check-input" id="radio2" name="${i[2]}" value="False">False</input>
    </div>`)
       a +=1
      break;
    case 'Free response':
      console.log('free response')
      $('#quiz').append(`<p class='q f frq bb${a}'>${i[0]}</p><label for="bb${a}" class="form-label q bb${a}">Answer:</label>
    <input style='display:none;width:80vw;' class="form-control q bb${a}" type='text' autosubmit='false' id="bb${a}" name='${i[2]}' required></input>`)
      console.log(a)
       a +=1
      break;
  }}
  catch(err) {
    alert('hi')
  }
}
var b = 1
var type = 1
function increment() {
  $('#p').fadeIn(300)

  const gh = document.getElementsByClassName('f').length
  console.log(gh)
  if (type == 0){
    b++
  }
  gg = String(Math.round(b/gh*100))+'%'
  type = 1
  if (b == gh){
    $('#i').css('display','none')
  }else{
    $('#i').fadeIn(300)
  }
  if (b> 1){
    $('#d').fadeIn(300)
  }else{
    $('#d').fadeOut(300)
  }
  g = '.bb'+b
  $('#bar').fadeIn(300)
  $('#bar').animate({'width':gg})
  $('#p').text(gg)
  $('#h').fadeOut(300)
  $('.q').fadeOut(300)
  $(g).fadeIn(300)
  b++
}
function decrement() {
  $('#p').fadeIn(300)
  const gh = document.getElementsByClassName('f').length
  b--
  if (type == 1){
    b--
  }
  type = 0

  if (b == gh){
    $('#i').css('display','none')
  }else{
    $('#i').fadeIn(300)
  }
  gg = String(Math.round(b/gh*100))+'%'
  if (b == gh){
    b--
  }
  if (b == 0 ){
    b = gh
  }
  if (b> 1){
    $('#d').fadeIn(300)
  }else{
    $('#d').css('display','none')
  }
  console.log(b)
  $('#p').text(gg)
  console.log(b)
  $('#bar').fadeIn(300)
  $('#bar').animate({'width':gg})
  $('#h').fadeOut(300)
  g = '.bb'+b
  $('.q').fadeOut(300)
  $(g).fadeIn(300)

}
function onstart(b) {
  try{
  $('#d').fadeOut(300)
  $('#p').fadeOut(300)
  questionno = 1
 $.getJSON("getjson2/"+b, function(result){
   console.log(result)
 for (let i = 0; i < result['questions'].length; i++) {
    render([result['questions'][i][0],result['questions'][i][1],result['questions'][i][2]],result['questions_mc'])
  }
  $('#quiz').append(`<button id='submit' type="submit" class='bb${a} h f q'>submit</button>`)
  });


}
  catch(err) {
  alert(err.message)
}
  }

//this bit was copy and past from stack overflow
 $(document).on("keydown", "form", function(event) { 
   console.log('called')
    return event.key != "Enter";
})