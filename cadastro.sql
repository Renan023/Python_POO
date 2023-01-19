
create database cadastro
default character set utf8
default collate utf8_general_ci;

use cadastro;

create table visitor(
ID int auto_increment not null primary key,
Nome varchar(100) not null,
Nasc int not null,  
Idade  int not null,
Sexo char(1) not null
) default charset = utf8;

select * from visitor;