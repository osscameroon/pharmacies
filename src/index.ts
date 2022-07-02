import express from "express";
import {getPharmacy, Item} from "./pharmacy"

const port: number = 4400;
const app = express();

const handleHome = async (req: any, res: any) => {
	const data = getPharmacy();

    res.send(data);
};

app.get("/", handleHome);
app.listen(port, () => {
  console.log(`The application is listening on port ${port}`);
});
