import React, { ReactNode } from 'react';
import { Sidebar } from '@/components/sidebar';
import { Footer } from '@/components/footer';
// Enhancement - 2025-03-09
// Enhancement - 2025-04-01
// Enhancement - 2025-04-04
// Enhancement - 2025-04-16
// Enhancement - 2025-04-18
// Enhancement - 2025-04-21
// Enhancement - 2025-04-22
// Enhancement - 2025-04-23
// Enhancement - 2025-04-26
// Enhancement - 2025-04-29
// Enhancement - 2025-06-09

interface DashboardLayoutProps {
  children: ReactNode;
}

export const DashboardLayout: React.FC<DashboardLayoutProps> = ({ children }) => {
  return (
    <div className="min-h-screen bg-background">
      <Sidebar />
      <div className="ml-64 min-h-screen"> {/* ml-64 equals the width of sidebar */}
        <main className="p-6 pb-16">
          {children}
        </main>
        <Footer />
      </div>
    </div>
  );
}; 