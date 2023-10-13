print("Started Adding the Users.");
print("OOOOOLAAAAAAAAAAAA");
conn = new Mongo();
db = conn.getDB("labels");

db.createUser({
  user: "root",
  pwd: "vitocox18",
  roles: [{ role: "readWrite", db: "labels" }],
});

print("End Adding the User Roles.");
