--cau 1
CREATE TYPE T_Diachi AS OBJECT
    (   ip VARCHAR(15),
        dns VARCHAR(100)
    );
    
CREATE TYPE T_Vitri AS OBJECT
    (   khuvuc VARCHAR(50),
        toanha VARCHAR(20),
        phong NUMBER(3)
    );
    
CREATE TYPE T_Quantri AS OBJECT
    (   idQt NUMBER(3),
        hoten VARCHAR(20)
    );
--cau 2
CREATE TABLE Maychu(
    id NUMBER(3),
    diachi T_Diachi,
    vitri T_Vitri
);

DESC maychu;

INSERT INTO maychu 
    VALUES (0,T_Diachi('159.84.143.204','www.ctu.edu.vn'),T_Vitri('Can Tho', 'C',1));
    
INSERT INTO maychu 
    VALUES (1,T_Diachi('172.16.167.204','www.cit.ctu.edu.vn'),T_Vitri('Can Tho', 'A',2));
INSERT INTO maychu 
    VALUES (2,T_Diachi('205.84.128.249','bdd.univ-lyon2.fr'),T_Vitri('Lyon', 'L',10));
INSERT INTO maychu 
    VALUES (3,T_Diachi('159.84.143.230','www.ctu.edu.vn'),T_Vitri('Can Tho', 'C',5));
INSERT INTO maychu 
    VALUES (4,T_Diachi('159.84.143.240','www.ctu.edu.vn'),T_Vitri('Can Tho', 'C',15));
INSERT INTO maychu 
    VALUES (5,T_Diachi('159.84.143.255','www.ctu.edu.vn'),T_Vitri('Can Tho', 'C',3));

SELECT p.diachi.dns    
     FROM maychu p;

SELECT p.diachi.ip, p.diachi.dns, p.vitri.khuvuc    
     FROM maychu p
     WHERE p.vitri.khuvuc = 'Can Tho';

--6
SELECT count(p.diachi.ip)soluong, p.vitri.toanha toanha   
     FROM maychu p
     group by p.vitri.toanha;
--7
CREATE TABLE NguoiQuanTri OF T_Quantri (primary key (idQt))
desc nguoiquantri;
--8
--    truc tiep
INSERT INTO nguoiquantri 
    VALUES (0,'Philip Iksal');
--    ham tao
INSERT INTO nguoiquantri 
    VALUES (T_Quantri(1,'Nathalie Coq'));

--9
SELECT value(p).hoten
     FROM nguoiquantri p;
--ham nay tra ve 1 doi tuong
--10
ALTER TABLE maychu
  ADD refQuantri REF T_Quantri;
desc maychu;
--11
SELECT *
    FROM maychu;
    
UPDATE maychu p SET p.refquantri = (
    SELECT REF(x) FROM nguoiquantri x where x.idqt = 0)
WHERE p.id = 0;
    
--12
--co nguoi quan tri
SELECT p.diachi.ip 
    FROM maychu p
    where p.refquantri is not DANGLING;
--khong nguoi quan tri
SELECT p.diachi.ip 
    FROM maychu p
    where p.refquantri is Null;
--13
UPDATE maychu p SET p.refquantri = (
    SELECT REF(x) FROM nguoiquantri x where x.idqt = 1)
WHERE p.id > 0;
    
SELECT
    * FROM maychu;
    
--14
SELECT p.diachi.dns
     FROM maychu p
     where p.refquantri.idQt =1;
--15
SELECT p.refquantri.hoten
    FROM maychu p
    WHERE p.vitri.khuvuc = 'Can Tho';
--16    
SELECT deref(p.refquantri)
    FROM maychu p
    WHERE p.id = 4
    
    
    