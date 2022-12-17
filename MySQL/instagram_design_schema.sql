DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS photos;

CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username VARCHAR(100) UNIQUE NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS photos(
id INTEGER PRIMARY KEY,
image_url VARCHAR(255) NOT NULL,
user_id INTEGER NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(user_id) REFERENCES users(id));

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