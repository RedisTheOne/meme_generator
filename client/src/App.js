import React, { useEffect, useContext, useState } from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import HomePage from './pages/HomePage'
import './styles/IndexStyle.css'
import './styles/NavbarStyle.css'
import TemplatesPage from './pages/TemplatesPage'
import { apiUrl } from './Globals'
import { Context } from './context/Context'
import LoadingComponent from './components/LoadingComponent'
import TemplatePage from './pages/TemplatePage'

function App() {
  const setData = useContext(Context)[1]
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    fetch(`${apiUrl}templates`)
      .then(res => res.json())
      .then(data => {
        setData(data)
        setIsLoading(false)
      })
  }, [setData, setIsLoading])

  if(isLoading)
    return <LoadingComponent />

  return (
    <div className="App">
      <BrowserRouter>
          <Switch>
            <Route path={'/'} exact component={HomePage} />
            <Route path={'/templates'} exact component={TemplatesPage} />
            <Route path={'/templates/:id'} exact component={TemplatePage} />
          </Switch>
        </BrowserRouter>
    </div>
  );
}

export default App;
