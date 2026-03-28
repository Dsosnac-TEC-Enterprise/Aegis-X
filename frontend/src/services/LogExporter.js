import * as FileSystem from 'expo-file-system';
import * as Sharing from 'expo-sharing';

export const exportSystemLogs = async () => {
    try {
        const response = await fetch('http://localhost:8000/system/logs');
        const data = await response.json();
        
        const fileUri = FileSystem.documentDirectory + data.filename;
        
        // Write the log content to a local temp file
        await FileSystem.writeAsStringAsync(fileUri, data.content, {
            encoding: FileSystem.EncodingType.UTF8,
        });

        // Open the native share sheet
        if (await Sharing.isAvailableAsync()) {
            await Sharing.shareAsync(fileUri);
        } else {
            alert("Sharing is not available on this device.");
        }
    } catch (error) {
        console.error("Export failed:", error);
        alert("Log export failed. Check Gateway connection.");
    }
};
