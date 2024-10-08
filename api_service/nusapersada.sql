--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Debian 16.4-1)
-- Dumped by pg_dump version 16.4 (Debian 16.4-1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: v1_customers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.v1_customers (
    customers_id bigint NOT NULL,
    customers_name character varying(100) NOT NULL
);


ALTER TABLE public.v1_customers OWNER TO postgres;

--
-- Name: v1_customers_customers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.v1_customers ALTER COLUMN customers_id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.v1_customers_customers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: v1_products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.v1_products (
    products_id bigint NOT NULL,
    products_name character varying(250) NOT NULL,
    products_code character varying(15) NOT NULL,
    products_price double precision,
    products_stock integer DEFAULT 0 NOT NULL,
    products_status character varying(11) DEFAULT '0'::character varying NOT NULL
);


ALTER TABLE public.v1_products OWNER TO postgres;

--
-- Name: v1_products_products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.v1_products ALTER COLUMN products_id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.v1_products_products_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: v1_sale_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.v1_sale_items (
    item_id bigint NOT NULL,
    item_price double precision,
    item_qty integer DEFAULT 0 NOT NULL,
    is_verify integer DEFAULT 0 NOT NULL,
    products_id bigint NOT NULL,
    sales_id bigint NOT NULL
);


ALTER TABLE public.v1_sale_items OWNER TO postgres;

--
-- Name: v1_sale_items_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.v1_sale_items ALTER COLUMN item_id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.v1_sale_items_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: v1_sales; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.v1_sales (
    sales_id bigint NOT NULL,
    sales_code character varying(15) NOT NULL,
    sales_date date,
    sale_items_total integer DEFAULT 0 NOT NULL,
    sale_price_total double precision,
    customers_id bigint NOT NULL
);


ALTER TABLE public.v1_sales OWNER TO postgres;

--
-- Name: v1_sales_sales_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.v1_sales ALTER COLUMN sales_id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.v1_sales_sales_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	v1	0001_initial	2024-09-10 07:16:16.09084+07
\.


--
-- Data for Name: v1_customers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.v1_customers (customers_id, customers_name) FROM stdin;
1	Apple
2	Google
3	Microsoft
4	Tesla
5	Nokia
6	Huawei
7	Samsung
8	Motorolla
9	Siemens
10	Xiaomi
11	Oppo
12	Vivo
13	Realme
14	Infinix
15	Docomo
16	Dell
17	Asus
18	Acer
19	Lenovo
20	Polytron
21	Fujitsu
22	Blackberry
23	Andromax
24	HP
25	HTC
\.


--
-- Data for Name: v1_products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.v1_products (products_id, products_name, products_code, products_price, products_stock, products_status) FROM stdin;
3	Esia Hidayah	22222222	7000.77	0	Hold
7	Realme G7	77777777	3000.1	0	0
5	Xiaomi Redmi	44444444	5000.5	4947	0
10	Vivo Y17	99999999	1000	4931	0
9	Oppo A39	88888888	1000	4939	0
6	Iphone 17 ProMax	55555555	4000.25	4934	0
2	Samsung Galaxy	11111111	8000	4916	0
1	Ultra Phone	00000000	9999.9	4902	Hold
4	Nokia Lumia	33333333	6000	4973	0
8	Sony XYZ	66666666	2000	4936	0
\.


--
-- Data for Name: v1_sale_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.v1_sale_items (item_id, item_price, item_qty, is_verify, products_id, sales_id) FROM stdin;
1	2000	5	0	8	1
2	5000.5	4	0	5	1
3	6000	3	0	4	1
4	1000	2	0	10	1
5	1000	1	0	9	1
6	2000	4	0	8	2
7	5000.5	4	0	5	2
8	6000	3	0	4	2
9	1000	2	0	10	2
10	1000	2	0	9	2
11	4000.25	10	0	6	2
12	2000	4	0	8	3
13	5000.5	4	0	5	3
14	6000	3	0	4	3
15	1000	2	0	10	3
16	1000	2	0	9	3
17	4000.25	10	0	6	3
18	8000	8	0	2	3
19	9999.9	1	0	1	3
20	2000	2	0	8	4
21	5000.5	3	0	5	4
22	6000	3	0	4	4
23	1000	5	0	10	4
24	1000	6	0	9	4
25	4000.25	7	0	6	4
26	8000	1	0	2	4
27	9999.9	8	0	1	4
28	2000	9	0	8	5
29	5000.5	3	0	5	5
30	6000	3	0	4	5
31	1000	8	0	10	5
32	1000	2	0	9	5
33	4000.25	7	0	6	5
34	8000	1	0	2	5
35	9999.9	6	0	1	5
36	2000	1	0	8	6
37	5000.5	1	0	5	6
38	6000	1	0	4	6
39	1000	1	0	10	6
40	1000	2	0	9	6
41	4000.25	1	0	6	6
42	8000	1	0	2	6
43	9999.9	1	0	1	6
44	2000	2	0	8	7
45	5000.5	1	0	5	7
46	6000	3	0	4	7
47	1000	4	0	10	7
48	1000	5	0	9	7
49	4000.25	6	0	6	7
50	8000	7	0	2	7
51	9999.9	8	0	1	7
52	2000	10	0	8	8
53	5000.5	9	0	5	8
54	6000	8	0	4	8
55	1000	7	0	10	8
56	1000	6	0	9	8
57	4000.25	5	0	6	8
58	8000	4	0	2	8
59	9999.9	3	0	1	8
60	2000	2	0	8	9
61	5000.5	2	0	5	9
62	6000	8	0	2	9
63	1000	2	0	10	9
64	1000	2	0	9	9
65	4000.25	2	0	6	9
66	8000	2	0	2	9
67	9999.9	2	0	1	9
68	2000	2	0	8	10
69	5000.5	2	0	5	10
70	6000	8	0	2	10
71	1000	2	0	10	10
72	1000	2	0	9	10
73	4000.25	2	0	6	10
74	8000	2	0	2	10
75	9999.9	2	0	1	10
76	2000	1	0	8	11
77	5000.5	1	0	5	11
78	6000	1	0	2	11
79	1000	1	0	10	11
80	1000	9	0	9	11
81	4000.25	1	0	6	11
82	8000	1	0	2	11
83	9999.9	9	0	1	11
84	2000	1	0	8	12
85	5000.5	1	0	5	12
86	6000	1	0	2	12
87	1000	1	0	10	12
88	1000	9	0	9	12
89	4000.25	1	0	6	12
90	8000	1	0	2	12
91	9999.9	9	0	1	12
92	2000	1	0	8	13
93	5000.5	3	0	5	13
94	6000	1	0	2	13
95	1000	3	0	10	13
96	1000	1	0	9	13
97	4000.25	3	0	6	13
98	8000	1	0	2	13
99	9999.9	3	0	1	13
100	2000	4	0	8	14
101	5000.5	2	0	5	14
102	6000	4	0	2	14
103	1000	4	0	10	14
104	1000	2	0	9	14
105	4000.25	2	0	6	14
106	8000	2	0	2	14
107	9999.9	4	0	1	14
108	9999.9	19	0	1	16
109	4000.25	3	0	6	17
110	8000	2	0	2	17
111	9999.9	1	0	1	17
112	1000	10	0	10	18
113	8000	8	0	2	18
114	2000	5	0	8	19
115	5000.5	5	0	5	19
116	1000	5	0	10	19
117	5000.5	2	0	5	20
118	4000.25	2	0	6	20
119	9999.9	2	0	1	20
120	5000.5	2	0	5	21
121	4000.25	1	0	6	21
122	2000	4	0	8	22
123	6000	4	0	2	22
124	1000	4	0	10	22
125	1000	4	0	9	22
126	8000	4	0	2	22
127	9999.9	9	0	1	23
128	2000	4	0	8	24
129	5000.5	2	0	5	24
130	6000	4	0	2	24
131	1000	4	0	10	24
132	1000	4	0	9	24
133	4000.25	1	0	6	24
134	8000	4	0	2	24
135	9999.9	9	0	1	24
136	2000	1	0	8	25
137	5000.5	1	0	5	25
138	6000	1	0	2	25
139	1000	1	0	10	25
140	1000	1	0	9	25
141	4000.25	1	0	6	25
142	8000	1	0	2	25
143	9999.9	1	0	1	25
152	2000	1	0	8	27
\.


--
-- Data for Name: v1_sales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.v1_sales (sales_id, sales_code, sales_date, sale_items_total, sale_price_total, customers_id) FROM stdin;
1	SC-11111111	2024-09-10	5	51002	1
2	SC-22222222	2024-09-10	6	90004.5	2
3	SC-33333333	2024-09-10	8	164004.4	3
4	SC-44444444	2024-09-10	8	164002.45	4
5	SC-555555555	2024-09-10	8	157002.65	5
6	SC-66666666	2024-09-10	8	38000.65	6
7	SC-77777777	2024-09-10	8	196001.2	7
8	SC-88888888	2024-09-10	8	208005.45	8
9	SC-99999999	2024-09-10	8	110001.3	9
10	SC-10101010	2024-09-09	8	110001.3	10
11	SC-11110000	2024-09-09	8	124999.849	11
12	SC-12121212	2024-09-09	8	124999.849	12
13	SC-13131313	2024-09-09	8	77001.95	13
14	SC-14141414	2024-09-09	8	112001.1	14
15	SC-15151515	2024-09-09	0	0	15
16	SC-16161616	2024-09-09	1	189998.1	16
17	SC-17171717	2024-09-09	3	38000.65	17
18	SC-18181818	2024-09-08	2	74000	18
19	SC-91919191	2024-09-08	3	40002.5	19
20	SC-20202020	2024-09-08	3	38001.3	20
21	SC-21212121	2024-09-08	2	14001.25	21
22	SC-22002200	2024-09-08	5	72000	22
23	SC-23232323	2024-09-08	1	89999.099	23
24	SC-24242424	2024-09-11	8	176000.349	24
25	SC-25252525	2024-09-12	8	37000.65	25
27	SC-test	2024-09-12	1	2000	1
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 1, true);


--
-- Name: v1_customers_customers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.v1_customers_customers_id_seq', 25, true);


--
-- Name: v1_products_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.v1_products_products_id_seq', 10, true);


--
-- Name: v1_sale_items_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.v1_sale_items_item_id_seq', 152, true);


--
-- Name: v1_sales_sales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.v1_sales_sales_id_seq', 27, true);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: v1_customers v1_customers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.v1_customers
    ADD CONSTRAINT v1_customers_pkey PRIMARY KEY (customers_id);


--
-- Name: v1_products v1_products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.v1_products
    ADD CONSTRAINT v1_products_pkey PRIMARY KEY (products_id);


--
-- Name: v1_sale_items v1_sale_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.v1_sale_items
    ADD CONSTRAINT v1_sale_items_pkey PRIMARY KEY (item_id);


--
-- Name: v1_sales v1_sales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.v1_sales
    ADD CONSTRAINT v1_sales_pkey PRIMARY KEY (sales_id);


--
-- Name: v1_sale_items_products_id_b6761281; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX v1_sale_items_products_id_b6761281 ON public.v1_sale_items USING btree (products_id);


--
-- Name: v1_sale_items_sales_id_78dcdbc1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX v1_sale_items_sales_id_78dcdbc1 ON public.v1_sale_items USING btree (sales_id);


--
-- Name: v1_sales_customers_id_16c6d425; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX v1_sales_customers_id_16c6d425 ON public.v1_sales USING btree (customers_id);


--
-- Name: v1_sale_items v1_sale_items_products_id_b6761281_fk_v1_products_products_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.v1_sale_items
    ADD CONSTRAINT v1_sale_items_products_id_b6761281_fk_v1_products_products_id FOREIGN KEY (products_id) REFERENCES public.v1_products(products_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: v1_sale_items v1_sale_items_sales_id_78dcdbc1_fk_v1_sales_sales_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.v1_sale_items
    ADD CONSTRAINT v1_sale_items_sales_id_78dcdbc1_fk_v1_sales_sales_id FOREIGN KEY (sales_id) REFERENCES public.v1_sales(sales_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: v1_sales v1_sales_customers_id_16c6d425_fk_v1_customers_customers_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.v1_sales
    ADD CONSTRAINT v1_sales_customers_id_16c6d425_fk_v1_customers_customers_id FOREIGN KEY (customers_id) REFERENCES public.v1_customers(customers_id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

