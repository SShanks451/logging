import Body from "./components/Body";
import Result from "./components/Result";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

function App() {
  const appRouter = createBrowserRouter([
    {
      path: "/",
      element: <Body />,
    },
    {
      path: "/results",
      element: <Result />,
    },
  ]);

  return <RouterProvider router={appRouter} />;
}

export default App;
