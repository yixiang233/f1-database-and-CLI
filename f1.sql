--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

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
-- Name: circuits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.circuits (
    circuitid integer NOT NULL,
    circuitref character varying(50),
    name character varying(50),
    location character varying(50),
    country character varying(50),
    lat numeric,
    lng numeric,
    alt numeric,
    url character varying(255)
);


ALTER TABLE public.circuits OWNER TO postgres;

--
-- Name: constructor_standings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.constructor_standings (
    raceid integer,
    constructorstandingid integer NOT NULL,
    constructorid integer,
    points integer,
    "position" integer,
    wins integer
);


ALTER TABLE public.constructor_standings OWNER TO postgres;

--
-- Name: constructors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.constructors (
    constructorid integer NOT NULL,
    constructorref character varying(50),
    name character varying(50),
    nationality character varying(50),
    url character varying(225)
);


ALTER TABLE public.constructors OWNER TO postgres;

--
-- Name: driver_standings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.driver_standings (
    driverstandingid integer NOT NULL,
    driverid integer,
    raceid integer,
    points integer,
    positions integer,
    wins integer
);


ALTER TABLE public.driver_standings OWNER TO postgres;

--
-- Name: drivers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.drivers (
    driverid integer NOT NULL,
    driverref character varying(50),
    forename character varying(50),
    surname character varying(50),
    dob date,
    nationality character varying(50),
    url character varying(225)
);


ALTER TABLE public.drivers OWNER TO postgres;

--
-- Name: lap_times; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lap_times (
    raceid integer,
    driverid integer NOT NULL,
    lap integer NOT NULL,
    "position" integer,
    "time" character(8),
    milliseconds integer
);


ALTER TABLE public.lap_times OWNER TO postgres;

--
-- Name: pit_stops; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pit_stops (
    raceid integer,
    driverid integer NOT NULL,
    stop integer NOT NULL,
    lap integer,
    "time" time without time zone,
    duration numeric,
    milliseconds integer
);


ALTER TABLE public.pit_stops OWNER TO postgres;

--
-- Name: qualifying; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.qualifying (
    qualityid integer NOT NULL,
    raceid integer,
    driverid integer,
    constructorid integer,
    number integer,
    "position" integer,
    q1 character(8),
    q2 character(8),
    q3 character(8)
);


ALTER TABLE public.qualifying OWNER TO postgres;

--
-- Name: races; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races (
    raceid integer NOT NULL,
    circuitid integer,
    year integer,
    round integer,
    name character varying(50),
    date date,
    "time" time without time zone,
    url character varying(255)
);


ALTER TABLE public.races OWNER TO postgres;

--
-- Name: results; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.results (
    resultid integer NOT NULL,
    raceid integer,
    driverid integer,
    constructorid integer,
    number integer,
    grid integer,
    "position" integer,
    positionorder integer,
    points integer
);


ALTER TABLE public.results OWNER TO postgres;

--
-- Name: seasons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.seasons (
    year integer NOT NULL,
    url character varying(225)
);


ALTER TABLE public.seasons OWNER TO postgres;

--
-- Name: status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.status (
    statusid integer NOT NULL,
    status character varying(50)
);


ALTER TABLE public.status OWNER TO postgres;

--
-- Name: circuits circuits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.circuits
    ADD CONSTRAINT circuits_pkey PRIMARY KEY (circuitid);


--
-- Name: constructor_standings constructor_standings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.constructor_standings
    ADD CONSTRAINT constructor_standings_pkey PRIMARY KEY (constructorstandingid);


--
-- Name: constructors constructors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.constructors
    ADD CONSTRAINT constructors_pkey PRIMARY KEY (constructorid);


--
-- Name: driver_standings driver_standings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.driver_standings
    ADD CONSTRAINT driver_standings_pkey PRIMARY KEY (driverstandingid);


--
-- Name: drivers drivers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.drivers
    ADD CONSTRAINT drivers_pkey PRIMARY KEY (driverid);


--
-- Name: lap_times lap_times_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lap_times
    ADD CONSTRAINT lap_times_pkey PRIMARY KEY (driverid, lap);


--
-- Name: pit_stops pit_stops_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pit_stops
    ADD CONSTRAINT pit_stops_pkey PRIMARY KEY (driverid, stop);


--
-- Name: qualifying qualifying_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.qualifying
    ADD CONSTRAINT qualifying_pkey PRIMARY KEY (qualityid);


--
-- Name: races races_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT races_pkey PRIMARY KEY (raceid);


--
-- Name: results results_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_pkey PRIMARY KEY (resultid);


--
-- Name: seasons seasons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.seasons
    ADD CONSTRAINT seasons_pkey PRIMARY KEY (year);


--
-- Name: status status_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.status
    ADD CONSTRAINT status_pkey PRIMARY KEY (statusid);


--
-- Name: constructor_standings constructor_standings_constructorid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.constructor_standings
    ADD CONSTRAINT constructor_standings_constructorid_fkey FOREIGN KEY (constructorid) REFERENCES public.constructors(constructorid);


--
-- Name: constructor_standings constructor_standings_raceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.constructor_standings
    ADD CONSTRAINT constructor_standings_raceid_fkey FOREIGN KEY (raceid) REFERENCES public.races(raceid);


--
-- Name: driver_standings driver_standings_driverid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.driver_standings
    ADD CONSTRAINT driver_standings_driverid_fkey FOREIGN KEY (driverid) REFERENCES public.drivers(driverid);


--
-- Name: driver_standings driver_standings_raceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.driver_standings
    ADD CONSTRAINT driver_standings_raceid_fkey FOREIGN KEY (raceid) REFERENCES public.races(raceid);


--
-- Name: lap_times lap_times_driverid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lap_times
    ADD CONSTRAINT lap_times_driverid_fkey FOREIGN KEY (driverid) REFERENCES public.drivers(driverid);


--
-- Name: lap_times lap_times_raceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lap_times
    ADD CONSTRAINT lap_times_raceid_fkey FOREIGN KEY (raceid) REFERENCES public.races(raceid);


--
-- Name: pit_stops pit_stops_driverid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pit_stops
    ADD CONSTRAINT pit_stops_driverid_fkey FOREIGN KEY (driverid) REFERENCES public.drivers(driverid);


--
-- Name: pit_stops pit_stops_raceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pit_stops
    ADD CONSTRAINT pit_stops_raceid_fkey FOREIGN KEY (raceid) REFERENCES public.races(raceid);


--
-- Name: qualifying qualifying_constructorid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.qualifying
    ADD CONSTRAINT qualifying_constructorid_fkey FOREIGN KEY (constructorid) REFERENCES public.constructors(constructorid);


--
-- Name: qualifying qualifying_driverid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.qualifying
    ADD CONSTRAINT qualifying_driverid_fkey FOREIGN KEY (driverid) REFERENCES public.drivers(driverid);


--
-- Name: qualifying qualifying_raceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.qualifying
    ADD CONSTRAINT qualifying_raceid_fkey FOREIGN KEY (raceid) REFERENCES public.races(raceid);


--
-- Name: races races_circuitid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT races_circuitid_fkey FOREIGN KEY (circuitid) REFERENCES public.circuits(circuitid);


--
-- Name: results results_constructorid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_constructorid_fkey FOREIGN KEY (constructorid) REFERENCES public.constructors(constructorid);


--
-- Name: results results_driverid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_driverid_fkey FOREIGN KEY (driverid) REFERENCES public.drivers(driverid);


--
-- Name: results results_raceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_raceid_fkey FOREIGN KEY (raceid) REFERENCES public.races(raceid);


--
-- PostgreSQL database dump complete
--

