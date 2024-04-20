import { useState, useEffect } from "react";
import axios from "axios";

const Result = () => {
  const [result, setResult] = useState(null);
  const [images, setImages] = useState(null);

  const func = async () => {
    const getResponse = await axios.get("http://localhost:3000/api/results");
    const getImages = await axios.get("http://localhost:3000/api/save_images");
    setResult(getResponse);
    setImages(getImages.data);
  };

  useEffect(() => {
    func();
  }, []);

  if (!result || !images) {
    return (
      <div>
        <div className="text-center m-6 text-4xl font-semibold bg-slate-400 py-4">Results</div>
        <div className="text-center font-semibold text-4xl mt-40">Generating Results...</div>
      </div>
    );
  }

  return (
    <div>
      <div>
        <div className="text-center m-6 text-4xl font-semibold bg-slate-400 py-4">Results</div>
      </div>
      <div className="flex">
        <div>
          <img className="" src={images.cld_result_one} />
        </div>
        <div className="">
          <img className="mt-[34%]" src={images.cld_result_two} />
        </div>
        <div className="">
          <img className="mt-[21.5%]" src={images.cld_result_three} />
        </div>
        <div className="">
          <img className="mt-[21.5%]" src={images.cld_result_four} />
        </div>
        <div className="">
          <img className="mt-[21.5%]" src={images.cld_result_five} />
        </div>
        <div className="">
          <img className="mt-[34%]" src={images.cld_result_six} />
        </div>
      </div>
    </div>
  );
};

export default Result;