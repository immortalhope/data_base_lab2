INSERT INTO class_info
   (
	SELECT DISTINCT
	CASE WHEN classprofilename IS NULL THEN '0' ELSE classprofilename end,
    CASE WHEN classlangname IS NULL THEN '0' ELSE classlangname end
    FROM tbl_open_data_zno
);



INSERT into test_year
(
    SELECT
    DISTINCT year
    FROM tbl_open_data_zno
);



INSERT INTO birth_year
(
    SELECT DISTINCT
    birth
    FROM tbl_open_data_zno
);


INSERT INTO ter_type(
    SELECT DISTINCT
    tertypename
    FROM tbl_open_data_zno
);


INSERT INTO student_location(
    SELECT DISTINCT
    regname      ,
    areaname     ,
    tername      ,
    tertypename
    FROM tbl_open_data_zno
);


INSERT INTO student_type(
    SELECT DISTINCT
	CASE WHEN regtypename IS NULL THEN '0' ELSE regtypename end
    FROM tbl_open_data_zno
);


INSERT INTO sex(
    SELECT DISTINCT
    sextypename
    FROM tbl_open_data_zno
);



INSERT INTO institution_location(
    SELECT DISTINCT
	CASE WHEN eoregname IS NULL THEN '0' ELSE eoregname end,
	CASE WHEN eoareaname IS NULL THEN '0' ELSE eoareaname end,
	CASE WHEN eotername IS NULL THEN '0' ELSE eotername end
    FROM tbl_open_data_zno
);


INSERT INTO inst_type(
    SELECT DISTINCT
	CASE WHEN eotypename IS NULL THEN '0' ELSE eotypename end
    FROM tbl_open_data_zno
);



INSERT INTO education_institution(
    SELECT DISTINCT
	CASE WHEN eoname IS NULL THEN '0' ELSE eoname end,
	CASE WHEN eoparent IS NULL THEN '0' ELSE eoparent end,
	CASE WHEN eotypename IS NULL THEN '0' ELSE eotypename end,
	CASE WHEN eoregname IS NULL THEN '0' ELSE eoregname end,
	CASE WHEN eoareaname IS NULL THEN '0' ELSE eoareaname end,
	CASE WHEN eotername IS NULL THEN '0' ELSE eotername end
    FROM tbl_open_data_zno
);


INSERT INTO student
    (
    select
    outid             ,
    CASE WHEN eoname IS NULL THEN '0' ELSE eoname end,
    CASE WHEN classprofilename IS NULL THEN '0' ELSE classprofilename end,
    CASE WHEN classlangname IS NULL THEN '0' ELSE classlangname end,
    birth             ,
    CASE WHEN regtypename IS NULL THEN '0' ELSE regtypename end,
    sextypename       ,
    regname           ,
    areaname          ,
    tername           ,
    CASE WHEN eoparent IS NULL THEN '0' ELSE eoparent end,
    CASE WHEN eotypename IS NULL THEN '0' ELSE eotypename end,
	CASE WHEN eotername IS NULL THEN '0' ELSE eotername end
    from tbl_open_data_zno
    );






INSERT INTO test_info
    (SELECT
    outid,
    year,
    ukrtest,
    ukrteststatus,
    ukrball100,
    ukrball12,
    ukrball  ,
    tbl_open_data_zno.ukradaptscale    ,
    ukrptname       ,
    ukrptregname    ,
    ukrptareaname   ,
    ukrpttername    ,
    histtest        ,
    histlang        ,
    histteststatus  ,
    histball100     ,
    histball12      ,
    histball        ,
    histptname      ,
    histptregname   ,
    histptareaname  ,
    histpttername   ,
    mathtest        ,
    mathlang        ,
    mathteststatus  ,
    mathball100     ,
    mathball12      ,
    mathball        ,
    mathptname      ,
    mathptregname   ,
    mathptareaname  ,
    mathpttername   ,
    phystest        ,
    physlang        ,
    physteststatus  ,
    physball100     ,
    physball12      ,
    physball        ,
    physptname      ,
    physptregname   ,
    physptareaname  ,
    physpttername   ,
    chemtest        ,
    chemlang        ,
    chemteststatus  ,
    chemball100     ,
    chemball12      ,
    chemball        ,
    chemptname      ,
    chemptregname   ,
    chemptareaname  ,
    chempttername   ,
    biotest         ,
    biolang         ,
    bioteststatus   ,
    bioball100      ,
    bioball12       ,
    bioball         ,
    bioptname       ,
    bioptregname    ,
    bioptareaname   ,
    biopttername    ,
    geotest         ,
    geolang         ,
    geoteststatus   ,
    geoball100      ,
    geoball12       ,
    geoball         ,
    geoptname       ,
    geoptregname    ,
    geoptareaname   ,
    geopttername    ,
    engtest         ,
    engteststatus   ,
    engball100      ,
    engball12       ,
    engdpalevel     ,
    engball         ,
    engptname       ,
    engptregname    ,
    engptareaname   ,
    engpttername    ,
    fratest         ,
    frateststatus   ,
    fraball100      ,
    fraball12       ,
    fradpalevel     ,
    fraball         ,
    fraptname       ,
    fraptregname    ,
    fraptareaname   ,
    frapttername    ,
    deutest         ,
    deuteststatus   ,
    deuball100      ,
    deuball12       ,
    tbl_open_data_zno.deudpalevel     ,
    deuball         ,
    deuptname       ,
    deuptregname    ,
    deuptareaname   ,
    deupttername    ,
    spatest         ,
    spateststatus   ,
    spaball100      ,
    spaball12       ,
    spadpalevel     ,
    spaball         ,
    spaptname       ,
    spaptregname    ,
    spaptareaname   ,
    spapttername
    FROM tbl_open_data_zno
);

