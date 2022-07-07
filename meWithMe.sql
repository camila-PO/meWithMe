create database meWithMe;
use meWithMe;

create table inseguranca(
	codInsegura int not null primary key auto_increment,
    perg1 varchar(350) not null,
    perg2 varchar(350) not null,
    perg3 varchar(350) not null,
    perg4 varchar(350) not null,
    perg5 varchar(350) not null
)Engine = InnoDB;

select * from inseguranca;

create table rotulacao(
	codRotu int not null primary key auto_increment,
    perg6 varchar(350) not null,
    perg7 varchar(350) not null,
    perg8 varchar(350) not null,
    perg9 varchar(350) not null,
    perg10 varchar(350) not null
)Engine = InnoDB;

select * from rotulacao;