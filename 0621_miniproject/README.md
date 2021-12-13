<h1>🐶애견호텔 사이트🐶</h1>

<h2> 💪TEAM</h2>
&nbsp;DB테이블 구축 및 설계 : 반재광 <br>
&nbsp;frontend & backend : 이재선, 정주영A <br>

<h2> 📍구현기능</h2>
Python flask 동기/비동기 이용 </p>
DB연동을 통한 jwt token 생성 </p>


<h3><summary>1️⃣일차</summary></h3><details>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ oven을 사용한 웹페이지 구조 골격 설정 </p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 데이터베이스 구조 설정 및 sql 사용한 테이블 생성</p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ dao.py dto.py 생성</p>
</details>

<h3><summary>2️⃣일차</summary></h3><details>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 회원가입 페이지 생성, 기능구현(DB로 join 정보 저장)</p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 로그인 페이지 생성 </p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- token 반환 문제, DB 연동 필요</p>
</details>

<h3><summary>3️⃣일차</summary></h3><details>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 로그인 페이지 완료</p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 예약 페이지 생성 </p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 동일한 객실에 이미 예약이 있을경우 계약 할 수 없도록 기능 구현</p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 예약 확인 페이지 생성 및 완료</p>
</details>

<h3><summary>4️⃣일차</summary></h3><details>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 로그인 페이지 재확인</p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ home, about 페이지 이미지 삽입</p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ about 페이지 </p>
&nbsp;&nbsp;&nbsp;&nbsp; - 객실정보 table생성 비동기 구현 중</p>
&nbsp;&nbsp;&nbsp;&nbsp; ◼ 발표준비
</details>

<h2><summar> 📍 oven 구성</summary></h2>
  [oven](https://ovenapp.io/project/CihXFbKH6C5r19A9mIhFwBXJtqDCCF1B#NQ7MD/)


<h2><summary>💻Page 구성</summary></h2>
&nbsp;&nbsp;&nbsp;&nbsp;1) 메인 페이지 <br>
&nbsp;&nbsp;&nbsp;&nbsp;2) about 페이지 <br>
&nbsp;&nbsp;&nbsp;&nbsp;3) 회원가입 페이지 <br>
&nbsp;&nbsp;&nbsp;&nbsp;4) 로그인 페이지 <br>
&nbsp;&nbsp;&nbsp;&nbsp;5) 예약 페이지 <br>
&nbsp;&nbsp;&nbsp;&nbsp;6) 예약 확인페이지 <br>


<h2><summary>🧾Data base</summary></h2>
&nbsp;&nbsp;&nbsp;&nbsp;1) 회원 데이터 <br>
&nbsp;&nbsp;&nbsp;&nbsp;2) 객실 정보 데이터 <br>
&nbsp;&nbsp;&nbsp;&nbsp;3) 객실 type 정보 데이터 <br>
&nbsp;&nbsp;&nbsp;&nbsp;4) 강아지 데이터 <br>
&nbsp;&nbsp;&nbsp;&nbsp;5) 예약데이터 <br>

<br><br><br><hr><br><br><br>
<h2>🖥booking demo<h2>
  1. 기존 10개의 예약 table <br>
  <img src='https://github.com/dilatata/JavaScript/blob/main/0621_miniproject/img/bookng_1.PNG'> <br><br>
  2. 예약정보가 있는 객실과 날짜 중 예약이 된 객실의 예약과 checkindate 혹은 checkoutdate 가 겹치도록 설정 후 예약기능을 실행 <br>
  <img src='https://github.com/dilatata/JavaScript/blob/main/0621_miniproject/img/booking_2.PNG'><br><br>
  3. 입력한 예약정보가 db에 등록되지 않음을 확인<br>
  <img src='https://github.com/dilatata/JavaScript/blob/main/0621_miniproject/img/booking_3.PNG'><br><br>
  4. 예약정보가 있는 객실과 날짜 중 예약이 된 객실의 예약과 checkindate 혹은 checkoutdate 가 겹치지 않도록 설정 후 예약기능을 실행 <br>
  <img src='https://github.com/dilatata/JavaScript/blob/main/0621_miniproject/img/booking_4%2C.PNG'><br><br>
  5. 입력한 예약정보가 db에 등록되었음을 확인 가능<br>
  <img src='https://github.com/dilatata/JavaScript/blob/main/0621_miniproject/img/booking_5.PNG'><br><br>
  
  <br><br><br><hr><br><br><br>
  ➕더 필요한 기능들<br>
  - 예약, 회원가입 후 결과에 대한 정보(성공, 실패)를 반환하는 기능
  - jwt 생성 후 토큰의 storage 저장과 사용 기능
  - 아이디 중복 확인 및 방지 기능
  
  



