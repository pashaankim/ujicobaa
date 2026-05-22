import streamlit as st

st.title("🎈 uji coba kalkulator")
'use client';
  import { useState, useEffect } from 'react';
  import { evaluate } from 'mathjs';
  import 'katex/dist/katex.min.css';
  import { InlineMath, BlockMath } from 'react-katex';

export default function SmartPhysicsApp() {
  const [activeTab, setActiveTab] = useState('kalkulator');
  const [searchQuery, setSearchQuery] = useState('');

  // State untuk Kalkulator Newton
  const [massaNewton, setMassaNewton] = useState('5');
  const [percepatanNewton, setPercepatanNewton] = useState('2');
  const [gayaHasil, setGayaHasil] = useState(null);

  // State untuk Kalkulator Energi Kinetik
  const [massaEk, setMassaEk] = useState('2');
  const [kecepatanEk, setKecepatanEk] = useState('10');
  const [ekHasil, setEkHasil] = useState(null);

  // State untuk Converter
  const [convertValue, setConvertValue] = useState('100');
  const [convertType, setConvertType] = useState('kmjam_ms');
  const [convertResult, setConvertResult] = useState(null);

  // Efek perhitungan otomatis Hukum Newton
  useEffect(() => {
    if (massaNewton && percepatanNewton) {
      try {
        const hasil = evaluate(`${massaNewton} * ${percepatanNewton}`);
        setGayaHasil(hasil);
      } catch (e) { setGayaHasil('Error'); }
    } else { setGayaHasil(null); }
  }, [massaNewton, percepatanNewton]);

  // Efek perhitungan otomatis Energi Kinetik
  useEffect(() => {
    if (massaEk && kecepatanEk) {
      try {
        const hasil = evaluate(`0.5 * ${massaEk} * (${kecepatanEk} ^ 2)`);
        setEkHasil(hasil);
      } catch (e) { setEkHasil('Error'); }
    } else { setEkHasil(null); }
  }, [massaEk, kecepatanEk]);

  // Efek perhitungan otomatis Unit Converter
  useEffect(() => {
    if (convertValue) {
      try {
        let hasil;
        if (convertType === 'kmjam_ms') {
          hasil = evaluate(`${convertValue} * (1000 / 3600)`);
        } else if (convertType === 'j_kal') {
          hasil = evaluate(`${convertValue} * 0.239006`);
        } else if (convertType === 'm_cm') {
          hasil = evaluate(`${convertValue} * 100`);
        }
        setConvertResult(hasil.toFixed(2));
      } catch (e) { setConvertResult('Error'); }
    } else { setConvertResult(null); }
  }, [convertValue, convertType]);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 font-sans antialiased">
      {/* HEADER & HERO */}
      <header className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white py-12 px-4 shadow-md">
        <div className="max-w-4xl mx-auto text-center space-y-4">
          <h1 className="text-4xl font-extrabold tracking-tight"> Smart Physics Calculator</h1>
          <p className="text-blue-100 text-lg">Bukan cuma menghitung, tapi juga visualisasi konsep dan langkah belajar.</p>
          
          {/* Search Bar Mockup */}
          <div className="max-w-md mx-auto pt-4">
            <input 
              type="text" 
              placeholder="🔍 Cari rumus (misal: Energi Kinetik, Newton)..." 
              className="w-full px-4 py-3 rounded-full text-slate-800 shadow-inner focus:outline-none focus:ring-2 focus:ring-amber-400"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
        </div>
      </header>

      {/* NAVIGATION TABS */}
      <nav className="bg-white border-b sticky top-0 z-10 shadow-sm">
        <div className="max-w-4xl mx-auto flex justify-center space-x-1 p-2">
          {['kalkulator', 'library', 'converter'].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-6 py-2.5 rounded-lg text-sm font-medium capitalize transition-colors ${
                activeTab === tab 
                  ? 'bg-blue-600 text-white shadow' 
                  : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
              }`}
            >
              {tab === 'library' ? '📚 Formula Library' : tab === 'kalkulator' ? '🧮 Smart Calc' : '🔄 Converter'}
            </button>
          ))}
        </div>
      </nav>

      {/* MAIN CONTENT */}
      <main className="max-w-4xl mx-auto p-4 md:p-8">
        
        {/* TAB 1: SMART CALCULATOR */}
        {activeTab === 'kalkulator' && (
          <div className="space-y-8 animate-fadeIn">
            <div className="border-l-4 border-blue-600 pl-3">
              <h2 className="text-2xl font-bold">Modul Mekanika Dasar</h2>
              <p className="text-sm text-slate-500">Masukkan nilai yang kamu tahu, sistem akan menjabarkan jalannya rumus.</p>
            </div>

            <div className="grid md:grid-cols-2 gap-6">
              {/* Card 1: Hukum II Newton */}
              <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 space-y-4">
                <div className="flex justify-between items-center">
                  <h3 className="font-bold text-lg text-slate-800">Hukum II Newton</h3>
                  <span className="px-2 py-1 bg-blue-50 text-blue-600 text-xs font-semibold rounded">Mekanika</span>
                </div>
                <div className="bg-slate-50 p-2 rounded text-center">
                  <BlockMath math="F = m \cdot a" />
                </div>
                
                <div className="space-y-3">
                  <div>
                    <label className="block text-xs font-semibold text-slate-600 mb-1">Massa (m)</label>
                    <div className="relative">
                      <input type="number" className="w-full border p-2 rounded bg-slate-50/50" value={massaNewton} onChange={(e) => setMassaNewton(e.target.value)} />
                      <span className="absolute right-3 top-2 text-sm text-slate-400">kg</span>
                    </div>
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-600 mb-1">Percepatan (a)</label>
                    <div className="relative">
                      <input type="number" className="w-full border p-2 rounded bg-slate-50/50" value={percepatanNewton} onChange={(e) => setPercepatanNewton(e.target.value)} />
                      <span className="absolute right-3 top-2 text-sm text-slate-400">m/s^2</span>
                    </div>
                  </div>
                </div>

                {gayaHasil !== null && (
                  <div className="p-4 bg-emerald-50 rounded-xl border border-emerald-100 space-y-2">
                    <span className="text-xs font-bold text-emerald-700 uppercase tracking-wider">Hasil Akhir</span>
                    <p className="text-3xl font-black text-emerald-900">{gayaHasil} N</p>
                    <div className="text-xs text-slate-600 bg-white/80 p-2 rounded border border-emerald-50 font-mono space-y-1">
                      <p className="font-bold"> Langkah Penyelesaian:</p>
                      <p>1. <InlineMath math="F = m \cdot a" /></p>
                      <p>2. <InlineMath math={`F = ${massaNewton} \text{ kg} \cdot ${percepatanNewton} \text{ m/s}^2`} /></p>
                      <p>3. <InlineMath math={`F = ${gayaHasil} \text{ Newton (N)}`} /></p>
                    </div>
                  </div>
                )}
              </div>

              {/* Card 2: Energi Kinetik */}
              <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 space-y-4">
                <div className="flex justify-between items-center">
                  <h3 className="font-bold text-lg text-slate-800">Energi Kinetik</h3>
                  <span className="px-2 py-1 bg-blue-50 text-blue-600 text-xs font-semibold rounded">Energi</span>
                </div>
                <div className="bg-slate-50 p-2 rounded text-center">
                  <BlockMath math="E_k = \frac{1}{2} m v^2" />
                </div>
                
                <div className="space-y-3">
                  <div>
                    <label className="block text-xs font-semibold text-slate-600 mb-1">Massa benda (m)</label>
                    <div className="relative">
                      <input type="number" className="w-full border p-2 rounded bg-slate-50/50" value={massaEk} onChange={(e) => setMassaEk(e.target.value)} />
                      <span className="absolute right-3 top-2 text-sm text-slate-400">kg</span>
                    </div>
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-slate-600 mb-1">Kecepatan (v)</label>
                    <div className="relative">
                      <input type="number" className="w-full border p-2 rounded bg-slate-50/50" value={kecepatanEk} onChange={(e) => setKecepatanEk(e.target.value)} />
                      <span className="absolute right-3 top-2 text-sm text-slate-400">m/s</span>
                    </div>
                  </div>
                </div>

                {ekHasil !== null && (
                  <div className="p-4 bg-emerald-50 rounded-xl border border-emerald-100 space-y-2">
                    <span className="text-xs font-bold text-emerald-700 uppercase tracking-wider">Hasil Akhir</span>
                    <p className="text-3xl font-black text-emerald-900">{ekHasil} Joule</p>
                    <div className="text-xs text-slate-600 bg-white/80 p-2 rounded border border-emerald-50 font-mono space-y-1">
                      <p className="font-bold">✍️ Langkah Penyelesaian:</p>
                      <p>1. <InlineMath math="E_k = \frac{1}{2} m v^2" /></p>
                      <p>2. <InlineMath math={`E_k = \frac{1}{2} \cdot ${massaEk} \cdot (${kecepatanEk})^2`} /></p>
                      <p>3. <InlineMath math={`E_k = 0.5 \cdot ${massaEk} \cdot ${evaluate(`${kecepatanEk}^2`)}`} /></p>
                      <p>4. <InlineMath math={`E_k = ${ekHasil} \text{ Joule (J)}`} /></p>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: FORMULA LIBRARY */}
        {activeTab === 'library' && (
          <div className="space-y-6 animate-fadeIn">
            <div className="border-l-4 border-blue-600 pl-3">
              <h2 className="text-2xl font-bold">Daftar Rumus & Konstanta</h2>
              <p className="text-sm text-slate-500">Kumpulan pustaka rumus Fisika lengkap berskala SI.</p>
            </div>

            <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 space-y-4">
              <h3 className="text-xl font-bold text-indigo-900 border-b pb-2">🧠 Glosarium Rumus</h3>
              <div className="overflow-x-auto">
                <table className="w-full text-left text-sm text-slate-600">
                  <thead className="bg-slate-50 text-xs uppercase text-slate-700">
                    <tr>
                      <th className="p-3">Nama Rumus</th>
                      <th className="p-3">Simbol / Teori</th>
                      <th className="p-3">Keterangan Variabel</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y">
                    <tr>
                      <td className="p-3 font-semibold text-slate-900">Hukum II Newton</td>
                      <td className="p-3"><InlineMath math="F = m \cdot a" /></td>
                      <td className="p-3">F = Gaya (N), m = Massa (kg), a = Percepatan (<InlineMath math="m/s^2" />)</td>
                    </tr>
                    <tr>
                      <td className="p-3 font-semibold text-slate-900">Energi Kinetik</td>
                      <td className="p-3"><InlineMath math="E_k = \frac{1}{2}mv^2" /></td>
                      <td className="p-3">Ek = Energi (J), m = Massa (kg), v = Kecepatan (m/s)</td>
                    </tr>
                    <tr>
                      <td className="p-3 font-semibold text-slate-900">Energi Potensial</td>
                      <td className="p-3"><InlineMath math="E_p = m \cdot g \cdot h" /></td>
                      <td className="p-3">Ep = Energi (J), g = Gravitasi (<InlineMath math="m/s^2" />), h = Ketinggian (m)</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            
            {/* Konstanta Fisika Penting */}
            <div className="bg-slate-900 text-slate-100 p-6 rounded-2xl shadow-md space-y-3">
              <h3 className="text-lg font-bold text-amber-400">⚡ Konstanta Fisika Esensial</h3>
              <div className="grid grid-cols-2 md:grid-cols-3 gap-4 font-mono text-xs">
                <div className="p-2 bg-slate-800 rounded">📍 Gravitasi Bumi (<InlineMath math="g" />) = 9.8 <InlineMath math="m/s^2" /></div>
                <div className="p-2 bg-slate-800 rounded">🚀 Kecepatan Cahaya (<InlineMath math="c" />) = <InlineMath math="3 \times 10^8 \text{ m/s}" /></div>
                <div className="p-2 bg-slate-800 rounded">🧲 Konstanta Planck (<InlineMath math="h" />) = <InlineMath math="6.626 \times 10^{-34} \text{ J}\cdot\text{s}" /></div>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: AUTO UNIT CONVERTER */}
        {activeTab === 'converter' && (
          <div className="space-y-6 animate-fadeIn max-w-md mx-auto">
            <div className="border-l-4 border-blue-600 pl-3">
              <h2 className="text-2xl font-bold">Auto Unit Converter</h2>
              <p className="text-sm text-slate-500">Konversi nilai satuan fisika secara instan tanpa ribet.</p>
            </div>

            <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Pilih Jenis Konversi</label>
                <select 
                  className="w-full border p-2 rounded bg-slate-50"
                  value={convertType}
                  onChange={(e) => setConvertType(e.target.value)}
                >
                  <option value="kmjam_ms">Kecepatan: km/jam ➔ m/s</option>
                  <option value="j_kal">Energi: Joule ➔ Kalori</option>
                  <option value="m_cm">Panjang: Meter ➔ Centimeter</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Masukkan Nilai Asal</label>
                <input 
                  type="number" 
                  className="w-full border p-2 rounded" 
                  value={convertValue} 
                  onChange={(e) => setConvertValue(e.target.value)} 
                />
              </div>

              {convertResult !== null && (
                <div className="p-4 bg-indigo-50 rounded-xl border border-indigo-100 text-center">
                  <span className="text-xs font-bold text-indigo-700 uppercase block mb-1">Hasil Konversi</span>
                  <p className="text-3xl font-black text-indigo-950 font-mono">
                    {convertResult} {convertType === 'kmjam_ms' ? 'm/s' : convertType === 'j_kal' ? 'kal' : 'cm'}
                  </p>
                </div>
              )}
            </div>
          </div>
        )}

      </main>
      
      <footer className="text-center py-8 text-xs text-slate-400 border-t mt-12 bg-white">
        Smart Physics Calculator Project MVP Engine © 2026.
      </footer>
    </div>
  );
}
