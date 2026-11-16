import 'package:flutter/material.dart';

class CamaraScreen extends StatelessWidget {
  const CamaraScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Capturar ECG'),
        backgroundColor: Colors.red[100],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.camera, size: 100, color: Colors.grey[400]),
            const SizedBox(height: 20),
            const Text(
              'Aquí irá la cámara del móvil',
              style: TextStyle(fontSize: 18, color: Colors.grey),
            ),
            const SizedBox(height: 40),
            ElevatedButton(
              onPressed: () {
                Navigator.pop(context); // Regresa a la pantalla anterior
              },
              child: const Text('Simular Captura'),
            ),
          ],
        ),
      ),
    );
  }
}
