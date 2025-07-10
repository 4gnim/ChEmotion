import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:logger/logger.dart';

class ApiService {
  static Future<Map<String, dynamic>?> predictStress(File imageFile) async {
    var logger = Logger(
      filter: null, // Use the default LogFilter (-> only log in debug mode)
      printer: PrettyPrinter(), // Use the PrettyPrinter to format and print log
      output: null, // Use the default LogOutput (-> send everything to console)
    );

    var uri = Uri.parse(
      "http://10.0.2.2:5000/predict",
    ); // gunakan 10.0.2.2 jika emulator Android
    var request = http.MultipartRequest('POST', uri);
    request.files.add(
      await http.MultipartFile.fromPath('image', imageFile.path),
    );

    try {
      var streamedResponse = await request.send();
      var response = await http.Response.fromStream(streamedResponse);

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        logger.w("Server error: ${response.statusCode}");
        return null;
      }
    } catch (e) {
      logger.w("Request failed: $e");
      return null;
    }
  }
}
