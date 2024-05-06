import express from "express";
import cors from "cors";
import multer from "multer";
import { spawn } from "child_process";
import fs from "fs";
import { v2 as cloudinary } from "cloudinary";

const app = express();

app.use(cors());

app.use(express.json());

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    return cb(null, "./las-file");
  },
  filename: function (req, file, cb) {
    return cb(null, "well_data.las");
  },
});

const upload = multer({ storage });

app.post("/api/upload", upload.single("file"), (req, res) => {
  // console.log(req.file);
});

app.post("/api/input_data", (req, res) => {
  fs.writeFileSync("input_data.json", JSON.stringify(req.body));
});

app.get("/api/results", (req, res) => {
  let output = "";
  const childPython = spawn("python", ["model.py", "input_data.json"]);

  childPython.stdout.on("data", (data) => {
    output += data.toString();
    console.log(output);
  });

  childPython.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  childPython.on("close", (code) => {
    console.log(`child process exited with code ${code}`);
    res.send("child process done");
  });
});

const img_one = "Gamma_ray_log_borehole_size_calliper_log.png";
const img_two = "Shale_volume.png";
const img_three = "Deep_Res.png";
const img_four = "Neutron_Density.png";
const img_five = "Shear_Compressional.png";
const img_six = "Neutron_Porosity_Density_Porosity.png";
const img_seven = "Sonic_Porosity.png";
const img_eight = "SwArch.png";

app.get("/api/save_images", async (req, res) => {
  const cld_result_one = await cloudinary.uploader.upload(img_one);
  const cld_result_two = await cloudinary.uploader.upload(img_two);
  const cld_result_three = await cloudinary.uploader.upload(img_three);
  const cld_result_four = await cloudinary.uploader.upload(img_four);
  const cld_result_five = await cloudinary.uploader.upload(img_five);
  const cld_result_six = await cloudinary.uploader.upload(img_six);
  const cld_result_seven = await cloudinary.uploader.upload(img_seven);
  const cld_result_eight = await cloudinary.uploader.upload(img_eight);

  res.json({
    cld_result_one: cld_result_one.url,
    cld_result_two: cld_result_two.url,
    cld_result_three: cld_result_three.url,
    cld_result_four: cld_result_four.url,
    cld_result_five: cld_result_five.url,
    cld_result_six: cld_result_six.url,
    cld_result_seven: cld_result_seven.url,
    cld_result_eight: cld_result_eight.url,
  });
});

app.get("/api/download_excel", (req, res) => {
  res.download("./Calculations.xlsx");
});

app.listen(3000, () => {
  console.log("Listening on port 3000");
});
