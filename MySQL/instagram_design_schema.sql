DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS photos;
DROP TABLE IF EXISTS comments;

CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username VARCHAR(100) UNIQUE NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS photos(
id INTEGER PRIMARY KEY,
image_url VARCHAR(255) NOT NULL,
user_id INTEGER NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(user_id) REFERENCES users(id)
ON DELETE CASCADE);

CREATE TABLE IF NOT EXISTS comments(
id INTEGER PRIMARY KEY,
commented_text VARCHAR(255) NOT NULL,
user_id INTEGER NOT NULL,
photo_id INTEGER NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(user_id) REFERENCES users(id),
FOREIGN KEY(photo_id) REFERENCES photos(id)
ON DELETE CASCADE);

INSERT OR IGNORE INTO users
(username) VALUES
('Aadrik'),('Adhesht'),('Baalaaji'),('Bhakthavat'),('Charudutta'),('Daksh'),('Dhevaneyan'),('Erran'),('Ezhumalai'),('Fatik'),('Farishta'),
('Aarv'),('Adhiraj'),('Balamurli'),('Bhanukiran'),('Charuvrat'),('Dakshit'),('Dhirendra'),('Eelamyntha'),('Fanibhusha'),('Fateh'),('Geethik'),
('Aatreya'),('Adikavi'),('Balagovind'),('Bhartesh'),('Cheliyan'),('Daivit'),('Dhruddavra'),('Ekambaram'),('Eniyan'),('Fhazaar'),('Gaalav'),
('Aarksh'),('Adisesh'),('Balamani'),('Bhautik'),('Chevatkodi'),('Deekshith'),('Digvijay'),('Ekaraj'),('Elakkiyan'),('Fanish'),('Ganak'),
('Aadish'),('Aditeya'),('Banbhatt'),('Chaitan'),('Chayank'),('Deepankar'),('Divinantha'),('Eklavya'),(' Boys from'),('Fanindra'),('Gambhir'),
('Aabheer'),('Advaya'),('Banuteja'),('Chinmay'),('Chidambar'),('Denadayal'),('Duranjaya'),('Elamurugu'),('abet'),('Faisal'),('Gabith'),
('Aadarsh'),('Agasti'),('Bargav'),('Ceyone'),('Chiranjeev'),('Devadatta'),('Durgadas'),('Elangovan'),('Farhat'),('Fani'),('Giaan'),
('Aagam'),('Agendra'),('Basavaraj'),('Charish'),('Chittranja'),('Devendrana'),('Dushyant'),('Elilaendhi'),('Fanishwar'),('Fenil'),('Govardhan'),
('Abhyudh'),('Baladitya'),('Bhaagavat'),('Charvik'),('Chyavan'),('Deveshwar'),('Ehan'),('Emmanuel'),('Fravash'),('Falish'),('Gowshik'),
('Achyuta'),('Bharat'),('Bhadraksh'),('Chezian'),('Chittesh'),('Dhanaditya'),('Esh/Eshwar'),('Eruyarthth'),('Frany'),('Firoz'),('Greeshkand'),
('Adeep'),('Bhavish'),('Bhagesh'),('Chandragup'),('Chitrasen'),('Dhanakoti'),('Eashan'),('Erisudar'),('Falgu'),('Fajyaz'),('Grishmith'),
('Adharva'),('Bhargava'),('Bhaidyanat'),('Chanyana'),('Chithayu'),('Dharmanand'),('Easwaran'),('Eshwinraj'),('Faneemdra'),('Faiz'),('Govindaraj');

INSERT OR IGNORE INTO photos
(image_url,user_id) VALUES
('http://WyMIcDVXF4O5fA3OSfoT',104),
('http://PcYAW31yi6pHjkELc5SL',94),('http://1gArzm8ES9h05ONjCRJf',81),('http://m90lslErDo7IOf27rZWP',119),('http://PBWZB3GZg52X6j9SVR96',42),
('http://R011uXwESk6F3cBdkO5Y',83),('http://RCTEzhuIhc9lGUGAl6xn',8),('http://NZJNbm05Xh4ZnfJ3EDdx',61),('http://VKSBGUQB2X5M1oiAEFcA',51),
('http://3o7eyCirLTubCIapL2SY',10),('http://ohpkwi2aWVPLagRKKlHg',9),('http://tM2GR0eEEYDGxtklBtnD',114),('http://foUxfned6Fjt5KmiWymc',118),
('http://tIIcvzGGbkalGuYr8Tis',84),('http://C5707rBuPpQxdQQZqidW',32),('http://pVnLszvLDvgQRZG9Ig3l',131),('http://uNrDOFJAXbtsFkLAv7z0',97),
('http://ktyySY95W5U915NmC4Z5',59),('http://LRXkaLLzAVgoPGnfYMIQ',126),('http://Tfkr8eI414Kxd3RaBavB',37),('http://AGZafb6rBH4SvJvKatLI',88),
('http://TCJZ12SvlwJAfz91hEWh',78),('http://604oZVw8pUUJCRPNSUMQ',118),('http://XY7KIshMdSNwEZy5Dxkk',77),('http://HTnMqT4tqwbW0hGHCb8a',10),
('http://SxrBeSfh9ywd3rbiBAg9',20),('http://MRvdP79AkQX5NxIXNDdP',70),('http://3BLa6ROKPO0RFbFoPApB',10),('http://yzR3Fv1Yc213pm796Wxc',29),
('http://9GMECR06g5VqlMVCfuGd',94),('http://BFNoDcgMFjI3O4kDqU65',10),('http://ONZfiCMrBWVR3Q9shHZk',23),('http://WwgZVdWtJ0UJgILzA5No',109),
('http://0TlNT0izgYZkoQszT5LA',15),('http://jiPHFFhuJszD4UVwlDkV',93),('http://bqaevJA4Czr28BGlIssG',82),('http://aJgdbZ5F2Uypsh5nR4YJ',38),
('http://JtKBbyZ7iezyPjakfiCv',39),('http://W2aWk6d0boRwi6szEK3j',35),('http://OZQE5fVSdLGdIY2cHZ0E',111),('http://7bL3PJBGOUuGD1C1fmkK',85),
('http://6hu4IgRw0ijvhrhL3hF3',129),('http://PRLkacFU8ojs2hhHWu9D',116),('http://utkc3JSX8KuQTZ03J1Wp',30),('http://vp7Y7U7qUpaanljnJ26E',82),
('http://LWPOp4mykVaH5fOEcVuI',47),('http://nIgHUqGri88E0lh9mnxI',67),('http://EORXsO0M7efikU54h3Sc',86),('http://Dv853MozTZz0zXtvegGr',120),
('http://cz80Q9H1vXAEatuUznhm',82),('http://KemNJ5SPFJwCIdobKONP',22),('http://fdpgMNPrJomynotsYdpG',122),('http://sGItcQPsYv5RHqeCjN7b',36),
('http://dxd3uakCgLuDzq0szGd3',126),('http://SAeXjuX7OsjIRQSXqksy',103),('http://9QFYrAh0AglNoClEyOTI',44),('http://gmGTUU30KxQCmSu08wla',111),
('http://r6BSaRuRZcJXHzVOj7uI',21),('http://2WTHxj5xfTwX1YGpsQTz',21),('http://VGlBUZ9vYI6mj8QbMEYD',98),('http://4XZUTchkooGWnbjm5u3r',39),
('http://PuMJwdniMLVr21pMgUaY',99),('http://RTcA42kjl3utGbbqAoYy',63),('http://KDtaqyZNCOoUAxoRc5fj',13),('http://7Lld3ls4LNlgMKEy3XTS',65),
('http://jx6tSdfzkGgyovrcIUP5',69),('http://PQfGAKNa0o5uv2DA7Jmh',49),('http://xUuP95U2ElrdQPv2Wkwb',1),('http://c13wRFDxsE2NnbhUwzI0',87),
('http://uG2FaRYYv3qHjKuedIWV',89),('http://5gRvcWIYZh9B3bGNS21J',120),('http://Ge3kd2FFDzByo9q2dNcs',126),('http://f2LPPCWVrzFOp7T9N96l',8),
('http://BIKpHdQYeBYznV2CD0Qv',99),('http://HvsihMz41dPLlHnrkFJH',2),('http://Tymdkpa7e6HZ0AugspLa',123),('http://41jYI6enIqTsOGVqS9Ox',82),
('http://tWQTZ1y4GFnRNZABdfq1',27),('http://gU0Ral4h5QL1VaQbeA4B',117),('http://ZEUIipsWhWmm7M7HGezl',118),('http://rHnLTNNzQNE6BJA18MKM',43),
('http://1RSyD2HFKsJX24JHBdFR',123),('http://ewmmhaani8UoQhEbLnhi',39),('http://ZRn3SzQijSlLidWeovoR',34),('http://2cziE1UhKpx8dDQdhlvh',132),
('http://Q36H5B65gnXIEACUTU2e',78),('http://CzxjZksS2MTRfDopRbRr',54),('http://DFfDNbIyJBUWZVLO8HwE',29),('http://mUuUCDZ7GmGTI96ckOrO',34),
('http://Knt0dhChmDrIcT3rCceP',12),('http://yTppmZj24M6aKeSveMau',125),('http://e2JhavFgk5R7Fnhc9key',117),('http://TgsC4v8hl6IvkJDtUcR7',74),
('http://wQr8Ndp1JzjwzgiKQY6w',33),('http://6C07JdpJE1l95hhSVdYt',10),('http://xawIXwJwRsiyXWhD3Yhr',113),('http://MDeaxu1xuAHYCmsYhS1z',84),
('http://ja57jyVGvCItVyH5KuBs',104),('http://1m5yzyItCaO0UjIN1aNo',2),('http://gtICwj7AWsxrsbdVbjQf',124),('http://s8PyMpRdcOJhPG0r9rdr',87),
('http://FmETIzZ9vn2GCsi0tY5r',124),('http://xs9g7ZRKNTwv9gl8JGRZ',60),('http://zciVUa7e9VMgnaStqKFu',81),('http://ilCrdkOuPxw2DG48lD5w',31),
('http://b77c0WykvHxBJdeKxWZR',65),('http://41YKjtjKe01Ul9tlMKPs',52),('http://KYr3hjAB3BUneaLWEdex',59),('http://yl4uezPzt5XBiPaseb04',78),
('http://B67cuuhPmreChdctMk0d',86),('http://FHjEgUh3upCp72OTgWKJ',24),('http://ORV9CLhCY6yISWpPuALo',77),('http://mq8NW6tMWKcz8IxRQIMv',94),
('http://CeaTzVhNo8jus8ipBjKI',121),('http://aYxGBXSA3Z8Zw2Czu2mr',83),('http://PaE6R7fVKL7i9Ah4r70l',103),('http://VuEQJeP1WWqaPubw6bQ6',131),
('http://STDLQQgUwksbxY30C5Fn',119),('http://jWenCJqcUYllWEI3QIo8',6),('http://nq6pqeVHAP5sizO5ggXN',121),('http://NNNaBDgUPvTOoI7dtK7w',82),
('http://eKfBgJVUqQpcUapojrfD',131),('http://t372UaVJQajlaEKpTkad',128),('http://juTXEaLMmIzJgUOhrHqR',59),('http://S0xbiuD9W55Qwskzlb8F',111),
('http://yiTpYg5XP4dZQa7cJzVk',67),('http://qNXVKLq4dICIJu1DqRnr',86),('http://ax94H46YwfXOy6wMjutM',19),('http://zC2n9Bpt5ArQjSHTjbNP',105),
('http://Y69jQ6C34IwzIMTkf6bw',1),('http://mDAyf6tr02iYsMy7MVLH',62),('http://cdjfxDJuXuVXcCRDyD3k',18),('http://pXpIoQ2JRLzVMxI9nvsG',84),
('http://t1XDvKTYafuahOo8bzaU',15),('http://fnf4gtSH75NvKo5bXYoU',11),('http://66yvvsCovbwG8OKm5Eb5',95),('http://Xpf3dVkqb9Ss0ghZc7xr',11),
('http://0uYOnbTLyMgb4sQL7wvY',56),('http://W0715JfaoEdHYqxJaAs2',20),('http://f1CxClpFDxAW5Kht2UrI',28),('http://gQImQ7hWRPwo2x3GP8TP',37),
('http://BGft8NajuX7q1IeW1pX7',51),('http://JaWAJYq0XGHxrZ45FLYc',33),('http://AwSwPrcMwP69CT5O2NAi',32),('http://mZ6c6CwNzyFq0UVVc0cQ',92),
('http://ricNZLs5VAbOAs2vzohm',64),('http://hU9ojj67e6BuSp9wDGrN',46),('http://HHmvrTbLQrah4Lk3lT8W',40),('http://blbmjk9nv8fxfJECI5SA',12),
('http://2mnNHNAkrjS59Ees6rYl',88),('http://bJkgqFxa28wt23hFo3wo',115),('http://Qp0dOWKejgDxt6hTxuyA',98),('http://AdPBfF3LF6hOFDPaaQct',1),
('http://UflGwCZJoG1kT4Y4JjON',55),('http://JNuwTGKQjFHrJZdy4OTY',91),('http://C0SlgwgITnQsllxsNa4i',42),('http://GmCK6dlXEySkjuvrCxdE',82),
('http://GHAvhS0kb8nBwg7yxXoN',51),('http://K2x7f4IwInaWUTGpGBMr',88),('http://ETlOqdAIUCdxSbub1kzH',64),('http://lFrAvNwK1wfbXIzxDTVF',71),
('http://d3OgLnl9R3MkXb2h4xNN',42),('http://xjSltghrS73qRxhVbJ4C',1),('http://V6me64zBssGhC5cVDMqT',128),('http://Tn0a64dcwrxpJtKkfZB6',6),
('http://mO3mGDaM6CV7EnYYDMzg',131),('http://6lwPFxdXUcbt2AopgYcn',119),('http://4JbCP64ox1wziCfDjSht',11),('http://jH7PJNu3ZMPI8VwRXzsU',2),
('http://WSruFq7W36VoMSkB2sj2',132),('http://D38jT8DEi2GvEruBVsxm',40),('http://hWgibHXPP1adBpJ77QRa',67),('http://QpBajrTn0oV2oJCHsAkK',131),
('http://UBybgTEO7NHYfqd4IyLY',1),('http://VSLRaqKoUxIbjV19a5R7',6),('http://DQchI11JF5GxCHc8NwXn',94),('http://kLgBzPvvOvVndVdjQFRL',53),
('http://RbqX1qI2enNC9Cho2IUP',25),('http://jvxpmuq78AQ3897J4JyA',111),('http://PzZNXxN2XNAkh3gkXDhv',25),('http://xYkcgP8jNkRWSW1LQkPE',98),
('http://nUlszB5YIi2JWCA3TmJX',28),('http://LMjPrH9GsfbHB8qEqLGA',85),('http://8pyJyjKudlj4YW309qGy',87),('http://IvqNVoHB67WuWc4TBXy9',86),
('http://ec8t5orR7tqO3PPQwRTY',67),('http://OwYaQODCGCfiYJ68huEn',131),('http://URW9w2bHlhOSl0iRPKBj',109),('http://fvtd21dxk2UmLotKAL9l',33),
('http://DU2WhR1EIGPWuEa1PDhQ',40),('http://IKkfCGWxetiS3FCTxEdZ',131),('http://QQUsAnRgjwt8ywUZokW5',55),('http://RioXfLl3CDaqUfXy8yJo',63),
('http://OJGgPw6qCXhusmhJ0dGZ',50),('http://74hQViI6NWVH4bG0a5Hq',108),('http://DNX2r8emmbsm3XoPRcDg',18),('http://Dd3JR91hayyEdvsFZW4M',62),
('http://d5T6Iqj4XezDDwtXOElE',9),('http://hfqNjmONa5XUSY3yWv1O',47),('http://O8ADh61LYObvaUgCJKuE',77);


