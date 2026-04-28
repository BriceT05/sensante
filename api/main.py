# api/main.py
# API FastAPI pour SenSante- Assistant pre-diagnostic medical
from fastapi import FastAPI
# Creer l'application
app = FastAPI(
title="SenSante API",
description="Assistant pre-diagnostic medical pour le Senegal",
version="0.2.0"
)
# Route de base : verifier que l'API fonctionne
@app.get("/health")
def health_check():
    """Verification de l'etat de l'API."""
    return {
        "status": "ok",
        "message": "SenSante API is running"
}   

from pydantic import BaseModel, Field
#--- Schemas Pydantic--
class PatientInput(BaseModel):
    """Donnees d'entree : les symptomes d'un patient."""
age: int = Field(..., ge=0, le=120, description="Age en annees")
sexe: str = Field(..., description="Sexe : M ou F")
temperature: float = Field(..., ge=35.0, le=42.0,
description="Temperature en Celsius")
tension_sys: int = Field(..., ge=60, le=250,
description="Tension systolique")
toux: bool = Field(..., description="Presence de toux")
fatigue: bool = Field(..., description="Presence de fatigue")
maux_tete: bool = Field(..., description="Presence de maux de tete")
region: str = Field(..., description="Region du Senegal")
class DiagnosticOutput(BaseModel):
    """Donnees de sortie : le resultat du diagnostic."""
diagnostic: str = Field(..., description="Diagnostic predit")
probabilite: float = Field(..., description="Probabilite du diagnostic")
confiance: str = Field(..., description="Niveau de confiance")
message: str = Field(..., description="Recommandation")

import joblib
import numpy as np
#--- Charger le modele et les encodeurs au demarrage--
print("Chargement du modele...")
model = joblib.load("models/model.pkl")
le_sexe = joblib.load("models/encoder_sexe.pkl")
le_region = joblib.load("models/encoder_region.pkl")
feature_cols = joblib.load("models/feature_cols.pkl")
print(f"Modele charge : {type(model).__name__}")
print(f"Classes : {list(model.classes_)}")