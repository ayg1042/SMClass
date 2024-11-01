// 1. Ajax를 사용한 데이터 가져오기
// 2. 삭제
// 3. 추가
$(function(){
  var count = 0;
  // Ajax로 데이터 가져오기 버튼
  $(document).on('click', '#dataBtn', function(){
    $.ajax({
      url : "js/stuData.json",
      type : "get",
      data : "",
      dataType : "json",
      success : function(data){
        var json_data = ''
        for(var i = 0; i < data.length; i++){
          json_data +=`
          <tr id="${data[i].no}">
            <td>${data[i].no}</td>
            <td>${data[i].name}</td>
            <td>${data[i].kor}</td>
            <td>${data[i].eng}</td>
            <td>${data[i].math}</td>
            <td>${data[i].total}</td>
            <td>${data[i].avg}</td>
            <td>
              <button class="updateBtn">수정</button>
              <button class="delBtn">삭제</button>
            </td>
          </tr>
          `;
          count++;
        }
        $('#tbody').html(json_data);
      },
      erroe : function(){
        alert("데이터 불러오기 실패")
      }
    })
  })
  // 삭제
  $(document).on('click', '.delBtn', function(){
    var del_target = $(this).closest('tr').attr('id');
    $('#' + del_target).remove();
  })
  // 추가
  $(document).on('click', '#create', function(){
    var name = $("#name").val()
    var kor = $("#kor").val()
    var eng = $("#eng").val()
    var math = $("#math").val()
    console.log(name)
  })
})