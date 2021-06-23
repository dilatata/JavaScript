-- 
-- 
-- newownerid, newemail, newownername, newpassword, newadress, newphoneno
insert into dogowner values('abc', 'abc@naver.com', 'juyoung', '1234', 'youngin', 8212312345);
insert into dogowner values('bcd', 'bcd@naver.com', 'sam', '0987', 'youngin', 1023423452);
insert into dogowner values('cdf', 'cdf@naver.com', 'ally', '5678', 'seoul', 2342342322);
insert into dogowner values('dfg', 'dfg@naver.com', 'sujan', '4567', 'seoul', 23423345);
insert into dogowner values('fgh', 'fgh@naver.com', 'atom', '9876', 'seoul', 111111111);
insert into dogowner values('asd', 'asd@naver.com', 'loy', '2468', 'seoul', 222222222);
insert into dogowner values('sdf', 'sdf@naver.com', 'tom', '3456', 'seoul', 333333333);
insert into dogowner values('kkk', 'kkk@naver.com', 'luke', '1574', 'seoul', 444444444);
insert into dogowner values('qwe', 'qwe@naver.com', 'molly', '2345', 'seoul', 555555555);
insert into dogowner values('jak', 'jak@naver.com', 'jake', '5436', 'seoul', 666666666);

-- 
-- 
-- 

-- insert into dog values(DogName, OwnerId, DogSize, DogBreed)
insert into dog values('gru', 'abc', 10, 'mix');
insert into dog values('nabak', 'bcd', 16, 'bodder');
insert into dog values('bonggu', 'cdf', 7, 'shiba');
insert into dog values('bori', 'kkk', 18, 'jindo');
insert into dog values('yul', 'fgh', 30, 'labrador');
insert into dog values('coco', 'qwe', 6, 'bichon');


-- 
-- 
-- 
-- newroomtype, newlength, newwidth, newheight, newroomtypedesc
insert into RoomType values ('a_medium', 100, 150, 80, 'standard');
insert into RoomType values ('b_medium', 250, 200, 80, 'premium');
insert into RoomType values ('a_large', 200, 150, 120, 'standard');
insert into RoomType values ('b_large', 250, 200, 120, 'premium');

-- 
-- 
-- 
-- 

-- newroomno, newroomname, newroomtype, newprice, newroomdesc
insert into Room values ( 1 , 'a_medium', '기본중형', 30000, 'standard');
insert into Room values ( 2 , 'a_medium', '기본중형', 30000, 'standard');
insert into Room values ( 3 , 'b_medium', '고급중형', 35000, 'premium');
insert into Room values ( 4 , 'b_medium', '고급중형', 35000, 'premium');
insert into Room values ( 5 , 'a_large', '기본대형', 40000, 'standard');
insert into Room values ( 6 , 'a_large', '기본대형', 40000, 'standard');
insert into Room values ( 7 , 'b_large', '고급대형', 45000, 'premium');
insert into Room values ( 8 , 'b_large', '고급대형', 45000, 'premium');


-- 
-- 
-- 
-- 
-- newbookingid, newownerid, newroomno, newbookingdate, newchindate, newchoutdate, newcancel,newdogname, newdogsize, newdogbreed ,newprice
-- insert into Booking values(BookingId, OwnerId ,RoomNo, BookingDate, CheckInDate, CheckOutDate, Cancellation, DogName, DogSize. DogBreed, TotalPrice);
insert into Booking values(Booking_seq.nextval, 'dfg' , 7, '20/12/23', '20/12/25', '20/12/27', 0, 'bori', 18, 'bori', 90000);
insert into Booking values(Booking_seq.nextval, 'fgh' , 6, '21/01/13', '21/01/13', '21/01/16', 0, 'yul', 30, 'labrador', 120000);
insert into Booking values(Booking_seq.nextval, 'bcd' , 3, '21/02/23', '21/02/25', '21/02/27', 0, 'nabak', 16, 'bodder', 70000);
insert into Booking values(Booking_seq.nextval, 'cdf' , 1, '21/02/21', '21/02/23', '21/02/26', 0, 'bonggu', 7, 'shiba', 90000);
insert into Booking values(Booking_seq.nextval, 'cdf' , 1, '21/03/21', '21/04/12', '21/04/13', 0, 'bonggu', 7, 'shiba', 60000);
insert into Booking values(Booking_seq.nextval, 'qwe' , 2, '21/03/21', '21/04/12', '21/04/13', 0, 'coco', 6, 'bichon', 60000);
insert into Booking values(Booking_seq.nextval, 'fgh' , 8, '21/05/13', '21/05/30', '21/06/03', 0, 'yul', 30, 'labrador', 180000);
insert into Booking values(Booking_seq.nextval, 'bcd' , 5, '21/05/16', '21/05/25', '21/05/26', 1, 'nabak', 16, 'bodder', 80000);
insert into Booking values(Booking_seq.nextval, 'qwe' , 2, '21/06/01', '21/06/02', '21/06/03', 0, 'coco', 6, 'bichon', 60000);
insert into Booking values(Booking_seq.nextval, 'qwe' , 2, '21/06/02', '21/06/03', '21/06/06', 1, 'coco', 6, 'bichon', 90000);

commit;
