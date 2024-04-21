import sample_data from "../images/sample-data.png";
import formula_used from "../images/formula-used.png";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Body = () => {
  const navigate = useNavigate();

  const [shallow_point, setShallow_point] = useState("");
  const [deep_point, setDeep_point] = useState("");
  const [shale_value, setShale_value] = useState("");
  const [clean_value, setClean_value] = useState("");
  const [matrix_density, setMatrixDensity] = useState("");
  const [fluid_density, setFluid_density] = useState("");
  const [fluid_transit_time, setFluid_transit_time] = useState("");
  const [matrix_transit_time, setMatrix_transit_time] = useState("");
  const [correction_factor_value, setCorrection_factor_value] = useState("");
  const [true_formation_resistivity, setTrue_formation_resistivity] = useState("");
  const [tortuosity, setTortuosity] = useState("");
  const [cementation_exponent, setCementation_exponent] = useState("");
  const [saturation_exponent, setSaturation_exponent] = useState("");

  const [file, setFile] = useState();

  const submit_data_button = async () => {
    window.alert("Data submitted!!");
    await axios.post("http://localhost:3000/api/input_data", {
      shallow_point,
      deep_point,
      shale_value,
      clean_value,
      matrix_density,
      fluid_density,
      fluid_transit_time,
      matrix_transit_time,
      correction_factor_value,
      true_formation_resistivity,
      tortuosity,
      cementation_exponent,
      saturation_exponent,
    });
  };

  const upload_button = () => {
    const formData = new FormData();
    formData.append("file", file);
    window.alert("File Uploaded!!");
    axios
      .post("http://localhost:3000/api/upload", formData)
      .then((res) => {})
      .catch((er) => console.log(er));
  };

  return (
    <div>
      <div className="text-center m-4 text-4xl font-semibold bg-gray-400 py-5">Well Log Visualization</div>
      <div className="grid grid-cols-5 gap-4">
        <div className="col-span-2">
          <div className="w-11/12 h-fit border-2 border-solid border-slate-600 rounded-lg m-6 p-6">
            <h1 className="text-xl font-bold text-center">Sample data frame</h1>
            <img className="w-full" src={sample_data} />
          </div>
          <div className="w-11/12 h-fit border-2 border-solid border-slate-600 rounded-lg m-6 p-6">
            <h1 className="text-xl font-bold text-center">Formula used</h1>
            <img className="w-full" src={formula_used} />
          </div>
        </div>
        <div className="col-span-3">
          <div className="w-11/12 h-fit border-2 border-solid border-slate-600 rounded-lg m-6 p-6">
            <div className="grid grid-cols-5">
              <h1 className="flex col-span-2 text-xl font-bold">Depth Range</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Shallow Point</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={shallow_point}
                    onChange={(e) => setShallow_point(e.target.value)}
                  />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Deep Point</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={deep_point}
                    onChange={(e) => setDeep_point(e.target.value)}
                  />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Gamma Ray Log</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Shale value(max reading)</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={shale_value}
                    onChange={(e) => setShale_value(e.target.value)}
                  />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Clean value(min reading)</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={clean_value}
                    onChange={(e) => setClean_value(e.target.value)}
                  />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Bulk Density Log</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Matrix Density</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={matrix_density}
                    onChange={(e) => setMatrixDensity(e.target.value)}
                  />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Fluid Density</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={fluid_density}
                    onChange={(e) => setFluid_density(e.target.value)}
                  />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Sonic Log</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Fluid transit time</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={fluid_transit_time}
                    onChange={(e) => setFluid_transit_time(e.target.value)}
                  />
                </div>
                <div className="flex mb-2">
                  <h1 className="w-2/5">Matrix transit time</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={matrix_transit_time}
                    onChange={(e) => setMatrix_transit_time(e.target.value)}
                  />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Correction factor value</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={correction_factor_value}
                    onChange={(e) => setCorrection_factor_value(e.target.value)}
                  />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Archie's Equation</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Res. formation water(Rw)</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={true_formation_resistivity}
                    onChange={(e) => setTrue_formation_resistivity(e.target.value)}
                  />
                </div>
                <div className="flex mb-2">
                  <h1 className="w-2/5">Tortuosity(a)</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={tortuosity}
                    onChange={(e) => setTortuosity(e.target.value)}
                  />
                </div>
                <div className="flex mb-2">
                  <h1 className="w-2/5">Cementation exponent(m)</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={cementation_exponent}
                    onChange={(e) => setCementation_exponent(e.target.value)}
                  />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Saturation exponent(n)</h1>
                  <input
                    className="w-3/5 border-2 border-solid border-slate-600 rounded text-center"
                    type="text"
                    value={saturation_exponent}
                    onChange={(e) => setSaturation_exponent(e.target.value)}
                  />
                </div>
              </div>
            </div>
            <p className="mt-10 text-center text-xl font-semibold">
              Note: Porosity is taken as the RMS of porosity from bulk density and neutron porosity
            </p>
            <div className="flex justify-center">
              <button className="mt-4 text-lg font-semibold bg-slate-400 px-6 py-1" onClick={submit_data_button}>
                Submit Data
              </button>
            </div>
          </div>
          <div className="w-11/12 h-fit border-2 border-solid border-slate-600 rounded-lg m-6 p-6">
            <h1 className="text-center text-xl font-bold">Upload las file</h1>
            <div className="flex justify-center mt-3">
              <input type="file" onChange={(e) => setFile(e.target.files[0])} />
              <button className="border-2 bg-slate-400 px-6 font-semibold" type="button" onClick={upload_button}>
                Upload
              </button>
            </div>
          </div>
        </div>
      </div>
      <div className="flex justify-center">
        <button
          className="m-6 text-2xl font-semibold bg-slate-400 px-10 py-2 w-[25%] rounded-md"
          onClick={() => {
            navigate("/results");
          }}
        >
          Submit
        </button>
      </div>
    </div>
  );
};

export default Body;
