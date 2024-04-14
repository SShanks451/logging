const Body = () => {
  return (
    <div>
      <div className="grid grid-cols-5 gap-4">
        <div className="col-span-2">HELLO</div>
        <div className="col-span-3">
          <div className="w-11/12 h-fit border-2 border-solid border-slate-600 rounded-lg m-6 p-6">
            <div className="grid grid-cols-5">
              <h1 className="flex col-span-2 text-xl font-bold">Depth</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Shallow Point</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Deep Point</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Gamma ray log</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Shale value(max reading)</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Clean value(min reading)</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Bulk Density</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Matrix Density</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Fluid Density</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Sonic Log</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">Fluid transit time</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex mb-2">
                  <h1 className="w-2/5">Matrix transit time</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Correction factor value</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
              </div>
            </div>

            <div className="h-[2px] w-full bg-black my-6"></div>

            <div className="grid grid-cols-5">
              <h1 className="col-span-2 text-xl font-bold">Archie's Equation</h1>
              <div className="col-span-3">
                <div className="flex mb-2">
                  <h1 className="w-2/5">True formation resistivity</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex mb-2">
                  <h1 className="w-2/5">Tortuosity(a)</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex mb-2">
                  <h1 className="w-2/5">Cementation exponent(m)</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
                <div className="flex">
                  <h1 className="w-2/5">Saturation exponent(n)</h1>
                  <input className="w-3/5 border-2 border-solid border-slate-600 rounded text-center" type="text" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Body;
