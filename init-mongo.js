db.createUser({
  user: "root",
  pwd: "vitocox18",
  roles: [{ role: "readWrite", db: "labels" }]
});
