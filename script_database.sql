--criação da database
CREATE DATABASE pao_prosa;

--após criar a base e dar o comando use, execute o script abaixo
CREATE TABLE public.products (
	id serial4 NOT NULL,
	"name" varchar NOT NULL,
	description varchar NOT NULL,
	value float4 NOT NULL,
	available bool NULL DEFAULT false,
	CONSTRAINT products_pk PRIMARY KEY (id)
);
