import YAML from "yaml";
import * as fs from "fs";

const pharmacyFilePath = __dirname + "/res/pharmacy.yaml";

export interface Item {
  fav_languages?: string;
  pro_cam_languages?: string[];
  pro_abroad_languages?: string[];
  fav_frameworks?: string[];
  pro_cam_frameworks?: string[];
  pro_abroad_frameworks?: string[];
};

export interface Pharmacy {
  items?: Item[];
};

export const getPharmacy = (): Pharmacy => {
  try {
    const file = fs.readFileSync(pharmacyFilePath, "utf8");
    const pharmacy = YAML.parse(file);
    return {
      items: pharmacy.items,
    };
  } catch (err) {
    //replace this with a proper log
    //and proper http error handling
    console.error("Failed to parse file:", err);
  }

  return {};
};
