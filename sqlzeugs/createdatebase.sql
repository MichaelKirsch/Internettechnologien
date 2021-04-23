

DROP TABLE IF EXISTS station;


CREATE TABLE station (
  stationID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  coordsA varchar(30) NOT NULL,
  coordsL varchar(30) NOT NULL,
  location varchar(30) NOT NULL,
  type varchar(1) NOT NULL,
  description varchar(50) NOT NULL
);




INSERT INTO `station` (`stationID`, `coordsA`, `coordsL`, `location`, `type`, `description`) VALUES
(1, '47.71457225467146', '10.314338207244873', 'Kempten', 'B', 'Firmensitz'),
(2, '47.72426740349347', '10.316848754882812', 'Kempten', 'A', 'Außenstelle'),
(3, '47.882828716292344', '10.6264343852617', 'Kaufbeuren', 'V', 'Außenstelle'),
(4, '47.98036221803081', '10.1788330078125', 'Memmingen', 'B', 'Außenstelle'),
(5, '47.694697038966076', '10.038070678710938', 'Isny', 'A', 'Außenstelle'),
(6, '47.77941861197757', '10.616891384124756', 'Marktoberdorf', 'A', 'Außenstelle'),
(7, '47.514634612973694', '10.26755619153846', 'Sonthofen', 'V', 'Außenstelle'),
(8, '47.41029678060909', '10.275293827580754', 'Oberstdorf', 'A', 'Außenstelle'),
(9, '47.554643912647045', '10.022393703984562', 'Oberstaufen', 'A', 'Außenstelle'),
(10, '47.560841627466885', '10.21770143561298', 'Immenstadt', 'A', 'Außenstelle'),
(11, '47.569648', '10.700432800000044', 'Füssen', 'B', 'Außenstelle'),
(12, '47.550241351721596', '9.69220304476039', 'Lindau', 'B', 'Außenstelle');

