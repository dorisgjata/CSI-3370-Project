DROP TABLE IF EXISTS campusLocations CASCADE;
DROP TABLE IF EXISTS menu CASCADE;
DROP TABLE IF EXISTS periods CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS filters CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE campusLocations(
    locationId INT PRIMARY KEY,
    locationName TEXT,
    startHours TIME,
    endHours TIME
    );
CREATE TABLE menu(
    menuId INT PRIMARY KEY,
    menuDate DATE,
    menuName TEXT,
    fromDate DATE,
    toDate DATE,
    locationID INT REFERENCES campusLocations(locationId), 
    itemID INT REFERENCES items (itemId) 
);
CREATE TABLE periods(
    periodId INT PRIMARY KEY,
    periodName TEXT,
    periodCategory INT REFERENCES categories(categoryId)
   );
CREATE TABLE categories(
    categoryId INT PRIMARY KEY,
    categoryName TEXT,
    categoryItems INT REFERENCES items(itemId)
   );
CREATE TABLE items(
    itemId INT PRIMARY KEY,
    itemName TEXT,
    itemPortion TEXT,
    itemIngridents TEXT,
    itemNutrients TEXT,
    itemFilters INT REFERENCES filters(filterID)
);
CREATE TABLE filters(
    filterId INT PRIMARY KEY,
    filterName TEXT
);

CREATE TABLE users(
    userId INT PRIMARY KEY,
    userName TEXT,
    userPassword TEXT,
    userPreferences TEXT
);
DROP TABLE IF EXISTS  preferences CASCADE;
CREATE TABLE preferences(
    preferenceId INT PRIMARY KEY,
    preferenceCalories TEXT ,
    preferenceNutrients TEXT,
    preferenceFilters INT REFERENCES filters(filterID)
);
