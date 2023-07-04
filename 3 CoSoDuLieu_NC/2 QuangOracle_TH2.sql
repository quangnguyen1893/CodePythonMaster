Câu 1
create or replace type T_Kiemtra as OBJECT (
    idKT number(6),
    kieu varchar(15),
    ngay date,
    ketqua char(1)
);

create type TAB_Kiemtra as table of T_Kiemtra;

create or replace type T_Vandongvien as OBJECT (
    idVDV number(5),
    ho varchar(20),
    ten varchar(20),
    dsKiemtra TAB_Kiemtra
);

create type TAB_Vandongvien as table of T_Vandongvien;


create or replace type T_Doi as OBJECT (
    idDoi number(5),
    maNuoc varchar(3),
    monThethao varchar(15),
    dsVandongvien TAB_Vandongvien
);

Câu 2
create table Doi OF T_Doi 
nested table dsVandongvien store as VDV
(nested table dsKiemtra store as KT);

desc Doi;

Câu 3
insert into Doi
values(1, 'USA', '100m', TAB_Vandongvien(T_Vandongvien(1, 'Green', 'Maunce', TAB_Kiemtra(T_Kiemtra(1, 'Sangun', '3/11/2005', 'N'))),T_Vandongvien(2, 'Lewis', 'Carl', TAB_Kiemtra(T_Kiemtra(2, 'Sangun', '3/11/2005', 'N')))));

INSERT INTO Doi VALUES(2, 'USA', 'Basket',
  TAB_VanDongVien(
    T_VanDongVien(23, 'Jordan', 'Michael',
          TAB_Kiemtra(T_Kiemtra(3, 'Urinaire', '3/11/2005', 'N'))),
    T_VanDongVien(8, 'Bryant', 'Kobe',
          TAB_Kiemtra(T_Kiemtra(4, 'Urinaire', '3/11/2005', 'N'))),
    T_VanDongVien(34, 'O Neal', 'Shaquille',
          TAB_Kiemtra(T_Kiemtra(5, 'Urinaire', '3/11/2005', 'N')))));
          
insert into Doi
values(3, 'UK', '100m', TAB_Vandongvien(T_Vandongvien(4, 'Sphinx', 'Le', TAB_Kiemtra(T_Kiemtra(6, 'Sangun', '3/11/2005', 'P'),T_kiemtra(7, 'Sangun', '4/11/2005', 'N')))));

insert into Doi
values(4, 'UK', 'Aviron', TAB_Vandongvien(T_Vandongvien(5, 'Smith', 'John', TAB_Kiemtra(T_Kiemtra(8, 'Urimaire', '3/11/2005', 'N'))),T_Vandongvien(6, 'Smith', 'Jack', TAB_Kiemtra(T_Kiemtra(9, 'Urimaire', '3/11/2005', 'P'),T_kiemtra(10, 'Urimaire', '4/11/2005', 'P')))));

insert into Doi
values(5, 'FRA', 'Aviron', TAB_Vandongvien(T_Vandongvien(9, 'Dupond', 'Albert', TAB_Kiemtra(T_Kiemtra(11, 'Urimaire', '3/11/2005', 'N'))),T_Vandongvien(7, 'Martin', 'Maunce', TAB_Kiemtra(T_Kiemtra(12, 'Urimaire', '3/11/2005', 'N')))));

INSERT INTO Doi VALUES(6, 'FRA', 'Basket',
  TAB_VanDongVien(
    T_VanDongVien(10, 'Bilba', 'Jim',
          TAB_Kiemtra(T_Kiemtra(13, 'Urinaire', '3/11/2005', 'N'))),
    T_VanDongVien(11, 'Parker', 'Tony',
          TAB_Kiemtra(T_Kiemtra(14, 'Urinaire', '3/11/2005', 'N'))),
    T_VanDongVien(12, 'Diaw', 'Boris', TAB_Kiemtra())));
	

Câu 4
select p.manuoc, p.monthethao, vdv.ho, vdv.ten
from doi p, table(p.dsVandongvien) vdv;

Câu 5
select p.manuoc, p.monthethao, cursor(select vdv.ho, vdv.ten from doi p, table(p.dsVandongvien) vdv) from doi p;

Câu 6
select p.manuoc, p.monthethao, vdv.ho, vdv.ten 
from doi p, table(p.dsVandongvien) vdv
order by p.manuoc, vdv.ho, vdv.ten


-- câu 7
select p.manuoc, kt.idKT, kt.ngay
from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt;

-- Câu 9
select p.idDoi, vdv.ho, vdv.ten 
from doi p, table(p.dsVandongvien) vdv
where p.idDoi = 2

-- câu 10
select p.idDoi, vdv.idvdv, kt.idKT, kt.kieu,  kt.ngay, kt.ketqua
from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt
where p.idDoi = 3 and vdv.idvdv = 4

--câu 11
select count(vdv.idvdv) as sovandngvien
from doi p, table(p.dsVandongvien) vdv
where p.idDoi = 6;

-- câu 12
select p.manuoc, count(vdv.idvdv) as sovandngvien
from doi p, table(p.dsVandongvien) vdv
group by p.manuoc;

-- câu 13
select vdv.idvdv, vdv.ho, vdv.ten, count(kt.idKT) as solankiemtra
from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt
group by vdv.idvdv, vdv.ho, vdv.ten
order by vdv.ho, vdv.ten;

-- câu 14
select vdv.idvdv, vdv.ho, vdv.ten, count(kt.idKT) as solanduongtinh
from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt
where kt.ketqua = 'P'
group by vdv.idvdv, vdv.ho, vdv.ten
order by vdv.ho, vdv.ten;

-- câu 15
select p.manuoc, count(kt.idKT) as solanduongtinh
from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt
where kt.ketqua = 'P'
group by p.manuoc
order by p.manuoc;

-- câu 16
select vdv.idvdv, vdv.ho, vdv.ten, max(kt.ngay) as ngayktsaucung
from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt
group by vdv.idvdv, vdv.ho, vdv.ten
order by vdv.ho, vdv.ten;

-- câu 17
select h.iddoi, h.manuoc, h.solankiemtra
from (
  select p.iddoi, p.manuoc,  count(kt.idKT) as solankiemtra
  from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt 
  group by p.iddoi, p.manuoc
) h
where h.solankiemtra = (select  max(solankiemtra)
from (
  select p.iddoi, count(kt.idKT) as solankiemtra
  from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt 
  group by p.iddoi
) ); 

-- câu 18
select h.iddoi, h.manuoc
from (
select p.iddoi, p.manuoc, count(vdv.idvdv) as sovdv
from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt
group by  p.iddoi, p.manuoc
) h
where h.sovadv = h.solankiemtra;

-- câu 19
select p.iddoi, p.manuoc
from doi p
where p.iddoi not in (
  select distinct p.iddoi
  from doi p, table(p.dsVandongvien) vdv, table(vdv.dsKiemtra) kt
  where kt.ketqua = 'P');
