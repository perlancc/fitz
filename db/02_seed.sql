begin;

create schema if not exists extensions;
create extension if not exists citext with schema extensions;
create extension if not exists pgcrypto;

-- Create demo user
insert into fitz.users (user_id, email)
values (gen_random_uuid(), 'demo@fitz.local')
on conflict (email) do nothing;

-- Insert basic lookup data
insert into fitz.categories (name) values
('Tops'),('Bottoms'),('Outerwear'),('Shoes')
on conflict do nothing;

insert into fitz.brands (name) values
('Nike'),('Zara'),('Levi''s')
on conflict do nothing;

insert into fitz.colors (name, hex_code) values
('Black','#000000'),('Blue','#0000FF'),('White','#FFFFFF')
on conflict do nothing;

insert into fitz.seasons (name) values
('Fall'),('Winter')
on conflict do nothing;

insert into fitz.occasions (name) values
('Casual'),('Work')
on conflict do nothing;

commit;
