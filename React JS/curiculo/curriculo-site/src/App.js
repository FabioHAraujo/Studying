import React, { useState } from 'react';
import './App.css';

const languagesData = [
  {
    year: '2020',
    languages: [
      { name: 'JavaScript', achievements: ['Projeto X', 'Projeto Y'] },
      { name: 'Python', achievements: ['Projeto Z'] },
    ],
  },
  {
    year: '2021',
    languages: [
      { name: 'Java', achievements: ['Projeto A', 'Projeto B'] },
      { name: 'C++', achievements: ['Projeto C'] },
    ],
  },
  // Adicione mais anos e linguagens conforme necessário
];

const App = () => {
  const [selectedYear, setSelectedYear] = useState(languagesData[0]);

  const handleYearSelection = (yearData) => {
    setSelectedYear(yearData);
  };

  return (
    <div className="app-container">
      <div className="horizontal-tab">
        {languagesData.map((yearData) => (
          <div
            key={yearData.year}
            className={`tab ${selectedYear === yearData ? 'active' : ''}`}
            onClick={() => handleYearSelection(yearData)}
          >
            {yearData.year}
          </div>
        ))}
      </div>
      <div className="vertical-tab">
        {selectedYear.languages.map((language) => (
          <div key={language.name} className="tab">
            <img src={`URL_DA_IMAGEM_PARA_${language.name}`} alt={language.name} />
            <div className="language-name">{language.name}</div>
            <div className="language-achievements">
              {language.achievements.map((achievement, index) => (
                <div key={index}>{achievement}</div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
