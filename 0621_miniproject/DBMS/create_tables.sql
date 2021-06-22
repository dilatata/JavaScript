drop table DogOwner cascade constraints;
drop table Dog cascade constraints;
drop table RoomType cascade constraints;
drop table Room cascade constraints;
drop table Booking cascade constraints;

create table DogOwner(
    OwnerId varchar2(50), --pk
    Email varchar2(100), --uq
    OwnerName varchar2(50) NOT NULL,
    Password varchar2(255) NOT NULL,
    Address varchar2(200),
    PhoneNo number(12) NOT NULL,
    constraint pk_DogOnwer_OnwerId primary key(OwnerId),
    constraint uq_DogOwner_Email unique(Email)
);

create table Dog(
	DogName varchar2(50), --pk
	OwnerId varchar2(50) NOT NULL, --fk
	DogSize number(3) NOT NULL,
	DogBreed varchar2(50), 
	constraint pk_Dog_DogName primary key(DogName),
    constraint fk_Dog_OwnerName foreign key(OwnerId) references DogOwner(OwnerId)
);

create table RoomType(
    RoomType varchar2(50), --pk
    LengthSize number(5) NOT NULL,
    WidthSize number(5) NOT NULL,
    HeightSize number(5) NOT NULL,
    RoomTypeDesc varchar2(100),
    constraint pk_RoomType_RoomType primary key(RoomType)
);

create table Room(
    RoomNo number(4), --pk
    RoomType varchar2(50) NOT NULL, --fk
    RoomName varchar2(50) NOT NULL,
    RoomPrice number(10) NOT NULL,
    RoomDesc varchar2(100),
    constraint pk_Room_RoomNo primary key(RoomNo),
    constraint fk_Room_RoomType foreign key(RoomType) references RoomType(RoomType)
);

create table Booking(
    BookingId number, --pk
    OwnerId varchar2(50) NOT NULL, --fk
    RoomNo number(4) NOT NULL, --fk
    BookingDate date NOT NULL,
    CheckInDate date NOT NULL,
    CheckOutDate date NOT NULL,
    Cancellation char(1),
    DogName varchar2(50) NOT NULL,
    DogSize number(3) NOT NULL,
    DogBreed varchar2(50),
    TotalPrice number(10) NOT NULL,
    constraint pk_Booking_BookingId primary key(BookingId),
    constraint fk_Booking_OwnerId foreign key(OwnerId) references DogOwner(OwnerId),
    constraint fk_Booking_RoomNo foreign key(RoomNo) references Room(RoomNo),
    constraint ck_Booking_Cancellation check(Cancellation = '0' OR Cancellation = '1')
);
