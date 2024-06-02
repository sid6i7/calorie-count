import './App.css';
import {
  createBrowserRouter,
  createRoutesFromChildren,
  RouterProvider,
  Route
} from 'react-router-dom';
import { Layout } from './pages/Layout';
import { IdentifyFood } from './pages/IdentifyFood/IdentifyFood';


function App() {
  const routes = createRoutesFromChildren(
    <Route path='/' element={<Layout />}>
      <Route path='identify' element={<IdentifyFood />} />
    </Route>
  );

  const router = createBrowserRouter(routes);

  return (
    <RouterProvider router={router}>
      <div className="App">
        React App
      </div>
    </RouterProvider>
  );
}

export default App;
