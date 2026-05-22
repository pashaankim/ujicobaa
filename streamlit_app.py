import streamlit as st

st.title("🎈 uji coba kalkulator")
import { useState, useEffect } from 'react';
import { evaluate } from 'mathjs';

export default function NewtonCalculator() {
  const [massa, setMassa] = useState('');
  const [percepatan, setPercepatan] = useState('');
  const [gaya, setGaya] = useState(null);

  useEffect(() => {
    if (massa && percepatan) {
      try {
        // Menghitung F = m * a menggunakan math.js
        const hasil = evaluate(`${massa} * ${percepatan}`);
        setGaya(hasil);
      } catch (error) {
        setGaya('Error');
      }
    } else {
      setGaya(null);
    }
  }, [massa, percepatan]);

  return (
    <div className="p-6 max-w-md mx-auto bg-white dark:bg-slate-800 rounded-xl shadow-md space-y-4">
      <h2 className="text-xl font-bold text-slate-900 dark:text-white">Kalkulator Hukum II Newton</h2>
      <p className="text-sm text-slate-500">Rumus dasar: <span className="font-mono">F = m × a</span></p>
      
      <div className="space-y-2">
        <label className="block text-sm font-medium">Massa (m)</label>
        <div className="flex gap-2">
          <input 
            type="number" 
            placeholder="Contoh: 5" 
            className="border p-2 rounded w-full dark:bg-slate-700"
            value={massa}
            onChange={(e) => setMassa(e.target.value)}
          />
          <span className="p-2 bg-gray-100 dark:bg-slate-600 rounded">kg</span>
        </div>
      </div>

      <div className="space-y-2">
        <label className="block text-sm font-medium">Percepatan (a)</label>
        <div className="flex gap-2">
          <input 
            type="number" 
            placeholder="Contoh: 2" 
            className="border p-2 rounded w-full dark:bg-slate-700"
            value={percepatan}
            onChange={(e) => setPercepatan(e.target.value)}
          />
          <span className="p-2 bg-gray-100 dark:bg-slate-600 rounded">m/s²</span>
        </div>
      </div>

      {gaya !== null && (
        <div className="mt-4 p-4 bg-green-50 dark:bg-green-900/30 rounded-lg">
          <p className="text-sm font-semibold text-green-800 dark:text-green-400">Hasil Akhir:</p>
          <p className="text-2xl font-bold text-green-900 dark:text-white">{gaya} N</p>
          <div className="mt-2 text-xs text-slate-600 dark:text-slate-300">
            <p className="font-semibold">Langkah Pengerjaan:</p>
            <p>1. Tulis rumus: <span className="italic">F = m × a</span></p>
            <p>2. Masukkan nilai: <span className="italic">F = {massa || 0} kg × {percepatan || 0} m/s²</span></p>
            <p>3. Didapat hasil: <span className="font-bold">{gaya} Newton (N)</span></p>
          </div>
        </div>
      )}
    </div>
  );
}
